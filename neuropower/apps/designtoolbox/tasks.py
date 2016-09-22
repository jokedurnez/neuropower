from django.conf import settings
from .models import DesignModel
from designcore import design
from .forms import DesignRunForm
from celery import task, Celery
import os
from utils import probs_and_cons
import numpy as np

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neuropower.settings')
app = Celery('neuropower')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task
def GeneticAlgorithm(sid):
    print("running now...")
    desdata = DesignModel.objects.get(SID=sid)
    runform = DesignRunForm(None, instance=desdata)

    matrices = probs_and_cons(sid)
    desfile = desdata.desfile
    genfile = desdata.genfile
    onsetsfolder = desdata.onsetsfolder

    des = design.GeneticAlgorithm(
        # design specific
        ITI=[desdata.ITImin, desdata.ITImean, desdata.ITImax],
        TR=desdata.TR,
        L=desdata.L,
        P=matrices["P"],
        C=matrices["C"],
        stim_duration=desdata.stim_duration,
        weights=desdata.W,
        ConfoundOrder=desdata.ConfoundOrder,
        MaxRepeat=desdata.MaxRepeat,
        restnum=desdata.RestNum,
        restlength=desdata.RestDur,
        # general/defaulted
        rho=desdata.rho,
        Aoptimality=True if desdata.Aoptimality == 1 else False,
        saturation=True if desdata.Saturation == 1 else False,
        resolution=desdata.resolution,
        G=desdata.G,
        q=desdata.q,
        I=desdata.I,
        cycles=desdata.cycles,
        preruncycles=desdata.preruncycles,
        HardProb=desdata.HardProb,
        tapsfile=os.path.join(settings.MEDIA_ROOT, "taps.p"),
        gui_sid=sid,
        write_score=genfile,
        write_design=desfile
    )
    des.counter = 0

    # Responsive loop

    desdata = DesignModel.objects.get(SID=sid)
    runform = DesignRunForm(None, instance=desdata)
    form = runform.save(commit=False)
    form.running = 1
    form.save()

    # Create first generation
    des.GeneticAlgorithmInitiate()

    # Maximise Fe
    desdata = DesignModel.objects.get(SID=sid)
    if des.weights[0] > 0 and des.preruncycles > 0 and desdata.stop == 0:
        runform = DesignRunForm(None, instance=desdata)
        form = runform.save(commit=False)
        form.running = 2
        form.save()
        des.prerun = 'Fe'
        NatSel = des.GeneticAlgorithmNaturalSelection(
            cycles=des.preruncycles)
        des.FeMax = np.max(NatSel['Best'])

    # Maximise Fd
    desdata = DesignModel.objects.get(SID=sid)
    if des.weights[1] > 0 and des.preruncycles > 0 and desdata.stop == 0:
        runform = DesignRunForm(None, instance=desdata)
        form = runform.save(commit=False)
        form.running = 3
        form.save()
        des.prerun = 'Fd'
        NatSel = des.GeneticAlgorithmNaturalSelection(
            cycles=des.preruncycles)
        des.FdMax = np.max(NatSel['Best'])

    # Natural selection
    desdata = DesignModel.objects.get(SID=sid)
    if desdata.stop == 0:
        des.prerun = None
        runform = DesignRunForm(None, instance=desdata)
        form = runform.save(commit=False)
        form.running = 4
        form.save()
        NatSel = des.GeneticAlgorithmNaturalSelection(
            cycles=des.cycles)

        # Select optimal design
        Generation = NatSel['Generation']
        Best = NatSel['Best']

        OptInd = np.min(np.arange(len(Generation['F']))[
                        Generation['F'] == np.max(Generation['F'])])
        des.opt = {
            'order': Generation['order'][OptInd],
            'onsets': Generation['onsets'][OptInd],
            'F': Generation['F'][OptInd],
            'FScores': Best
        }

        desdata = DesignModel.objects.get(SID=sid)
        runform = DesignRunForm(None, instance=desdata)
        form = runform.save(commit=False)
        form.optimalorder = Generation['order'][OptInd]
        form.optimalonsets = Generation['onsets'][OptInd]

        # reset
        form.save()
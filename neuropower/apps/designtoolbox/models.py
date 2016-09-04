from __future__ import unicode_literals
from django.db import models
from picklefield.fields import PickledObjectField
import os
from django.conf import settings

#import tempfile

#temp_dir = tempfile.gettempdir()

class DesignModel(models.Model):
    SID = models.CharField(max_length=300,default="")
    ITI = models.FloatField(default=None, null=True, blank=True)
    ITImin = models.FloatField(default=None, null=True, blank=True)
    ITImax = models.FloatField(default=None, null=True, blank=True)
    TR = models.FloatField(default=None, null=True, blank=True)
    L = models.IntegerField(null=True, blank=True)
    S = models.IntegerField(null=True, blank=True)
    Call = models.BooleanField(default=False)
    Clen = models.IntegerField(default=0,null=True, blank=True)
    RestNum = models.IntegerField(default=0,null=True,blank=True)
    RestDur = models.FloatField(default=None,null=True,blank=True)
    # contrasts and probabilities
    P0 = models.FloatField(default=None, null=True, blank=True)
    P1 = models.FloatField(default=None, null=True, blank=True)
    P2 = models.FloatField(default=None, null=True, blank=True)
    P3 = models.FloatField(default=None, null=True, blank=True)
    P4 = models.FloatField(default=None, null=True, blank=True)
    P5 = models.FloatField(default=None, null=True, blank=True)
    P6 = models.FloatField(default=None, null=True, blank=True)
    P7 = models.FloatField(default=None, null=True, blank=True)
    P8 = models.FloatField(default=None, null=True, blank=True)
    P9 = models.FloatField(default=None, null=True, blank=True)
    C00 = models.FloatField(default=None, null=True, blank=True)
    C01 = models.FloatField(default=None, null=True, blank=True)
    C02 = models.FloatField(default=None, null=True, blank=True)
    C03 = models.FloatField(default=None, null=True, blank=True)
    C04 = models.FloatField(default=None, null=True, blank=True)
    C05 = models.FloatField(default=None, null=True, blank=True)
    C06 = models.FloatField(default=None, null=True, blank=True)
    C07 = models.FloatField(default=None, null=True, blank=True)
    C08 = models.FloatField(default=None, null=True, blank=True)
    C09 = models.FloatField(default=None, null=True, blank=True)
    C10 = models.FloatField(default=None, null=True, blank=True)
    C11 = models.FloatField(default=None, null=True, blank=True)
    C12 = models.FloatField(default=None, null=True, blank=True)
    C13 = models.FloatField(default=None, null=True, blank=True)
    C14 = models.FloatField(default=None, null=True, blank=True)
    C15 = models.FloatField(default=None, null=True, blank=True)
    C16 = models.FloatField(default=None, null=True, blank=True)
    C17 = models.FloatField(default=None, null=True, blank=True)
    C18 = models.FloatField(default=None, null=True, blank=True)
    C19 = models.FloatField(default=None, null=True, blank=True)
    C20 = models.FloatField(default=None, null=True, blank=True)
    C21 = models.FloatField(default=None, null=True, blank=True)
    C22 = models.FloatField(default=None, null=True, blank=True)
    C23 = models.FloatField(default=None, null=True, blank=True)
    C24 = models.FloatField(default=None, null=True, blank=True)
    C25 = models.FloatField(default=None, null=True, blank=True)
    C26 = models.FloatField(default=None, null=True, blank=True)
    C27 = models.FloatField(default=None, null=True, blank=True)
    C28 = models.FloatField(default=None, null=True, blank=True)
    C29 = models.FloatField(default=None, null=True, blank=True)
    C30 = models.FloatField(default=None, null=True, blank=True)
    C31 = models.FloatField(default=None, null=True, blank=True)
    C32 = models.FloatField(default=None, null=True, blank=True)
    C33 = models.FloatField(default=None, null=True, blank=True)
    C34 = models.FloatField(default=None, null=True, blank=True)
    C35 = models.FloatField(default=None, null=True, blank=True)
    C36 = models.FloatField(default=None, null=True, blank=True)
    C37 = models.FloatField(default=None, null=True, blank=True)
    C38 = models.FloatField(default=None, null=True, blank=True)
    C39 = models.FloatField(default=None, null=True, blank=True)
    C40 = models.FloatField(default=None, null=True, blank=True)
    C41 = models.FloatField(default=None, null=True, blank=True)
    C42 = models.FloatField(default=None, null=True, blank=True)
    C43 = models.FloatField(default=None, null=True, blank=True)
    C44 = models.FloatField(default=None, null=True, blank=True)
    C45 = models.FloatField(default=None, null=True, blank=True)
    C46 = models.FloatField(default=None, null=True, blank=True)
    C47 = models.FloatField(default=None, null=True, blank=True)
    C48 = models.FloatField(default=None, null=True, blank=True)
    C49 = models.FloatField(default=None, null=True, blank=True)
    C = PickledObjectField(default="")
    P = PickledObjectField(default="")
    rho = models.FloatField(default=0.3)
    W1 = models.FloatField(default=0.25)
    W2 = models.FloatField(default=0.25)
    W3 = models.FloatField(default=0.25)
    W4 = models.FloatField(default=0.25)
    W = PickledObjectField(default="")
    Aoptimality_c = ((1,"A-optimality"),(2,"D-optimality"))
    Aoptimality = models.IntegerField(choices=Aoptimality_c,default=1)
    Saturation_c = ((1,"Saturation"),(2,"No Saturation"))
    Saturation = models.IntegerField(choices=Saturation_c,default=1)
    resolution = models.FloatField(default=0.1)
    G = models.IntegerField(default=20)
    q = models.FloatField(default=0.01)
    I = models.IntegerField(default=4)
    cycles = models.IntegerField(default=200)
    preruncycles = models.IntegerField(default=50)
    ConfoundOrder = models.IntegerField(default=3)
    MaxRepeat = models.IntegerField(default=6)
    HardProb = models.BooleanField(default=False)
    stop = models.IntegerField(default=0)
    running = models.IntegerField(default=0)
    optimalorder = PickledObjectField(default="")
    optimalonsets = PickledObjectField(default="")
    mainpars = models.BooleanField(default=False)
    conpars = models.BooleanField(default=False)
    def __unicode__(self): # Python 3: __str__
        return "<DesignModel:%s>" %self.SID

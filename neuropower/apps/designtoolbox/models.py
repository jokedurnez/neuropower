from __future__ import unicode_literals
from django.db import models
from picklefield.fields import PickledObjectField
import os
from django.conf import settings

#import tempfile

#temp_dir = tempfile.gettempdir()

class DesignModel(models.Model):
    SID = models.CharField(max_length=300,default="")
    ITI = models.DecimalField(max_digits=5,decimal_places=3)
    TR = models.DecimalField(max_digits=5,decimal_places=3)
    L = models.IntegerField()
    S = models.IntegerField()
    Clen = models.IntegerField()
    # contrasts and probabilities
    P0 = models.IntegerField(default=0)
    P1 = models.IntegerField(default=0)
    P2 = models.IntegerField(default=0)
    P3 = models.IntegerField(default=0)
    P4 = models.IntegerField(default=0)
    P5 = models.IntegerField(default=0)
    P6 = models.IntegerField(default=0)
    P7 = models.IntegerField(default=0)
    P8 = models.IntegerField(default=0)
    P9 = models.IntegerField(default=0)
    C00 = models.IntegerField(default=0)
    C01 = models.IntegerField(default=0)
    C02 = models.IntegerField(default=0)
    C03 = models.IntegerField(default=0)
    C04 = models.IntegerField(default=0)
    C05 = models.IntegerField(default=0)
    C06 = models.IntegerField(default=0)
    C07 = models.IntegerField(default=0)
    C08 = models.IntegerField(default=0)
    C09 = models.IntegerField(default=0)
    C10 = models.IntegerField(default=0)
    C11 = models.IntegerField(default=0)
    C12 = models.IntegerField(default=0)
    C13 = models.IntegerField(default=0)
    C14 = models.IntegerField(default=0)
    C15 = models.IntegerField(default=0)
    C16 = models.IntegerField(default=0)
    C17 = models.IntegerField(default=0)
    C18 = models.IntegerField(default=0)
    C19 = models.IntegerField(default=0)
    C20 = models.IntegerField(default=0)
    C21 = models.IntegerField(default=0)
    C22 = models.IntegerField(default=0)
    C23 = models.IntegerField(default=0)
    C24 = models.IntegerField(default=0)
    C25 = models.IntegerField(default=0)
    C26 = models.IntegerField(default=0)
    C27 = models.IntegerField(default=0)
    C28 = models.IntegerField(default=0)
    C29 = models.IntegerField(default=0)
    C30 = models.IntegerField(default=0)
    C31 = models.IntegerField(default=0)
    C32 = models.IntegerField(default=0)
    C33 = models.IntegerField(default=0)
    C34 = models.IntegerField(default=0)
    C35 = models.IntegerField(default=0)
    C36 = models.IntegerField(default=0)
    C37 = models.IntegerField(default=0)
    C38 = models.IntegerField(default=0)
    C39 = models.IntegerField(default=0)
    C40 = models.IntegerField(default=0)
    C41 = models.IntegerField(default=0)
    C42 = models.IntegerField(default=0)
    C43 = models.IntegerField(default=0)
    C44 = models.IntegerField(default=0)
    C45 = models.IntegerField(default=0)
    C46 = models.IntegerField(default=0)
    C47 = models.IntegerField(default=0)
    C48 = models.IntegerField(default=0)
    C49 = models.IntegerField(default=0)

    C = models.CharField(max_length=300,default="")
    P = models.CharField(max_length=300,default="")
    rho = models.DecimalField(max_digits=5,decimal_places=3,default=0.3)
    W1 = models.DecimalField(max_digits=5,decimal_places=3,default=0.25)
    W2 = models.DecimalField(max_digits=5,decimal_places=3,default=0.25)
    W3 = models.DecimalField(max_digits=5,decimal_places=3,default=0.25)
    W4 = models.DecimalField(max_digits=5,decimal_places=3,default=0.25)
    Aoptimality_c = ((1,"A-optimality"),(2,"D-optimality"))
    Aoptimality = models.IntegerField(choices=Aoptimality_c,default=1)
    Saturation_c = ((1,"Saturation"),(2,"No Saturation"))
    Saturation = models.IntegerField(choices=Saturation_c,default=1)
    resolution = models.DecimalField(max_digits=5,decimal_places=3,default=0.1)
    G = models.IntegerField(default=20)
    q = models.DecimalField(max_digits=5,decimal_places=3,default=0.01)
    I = models.IntegerField(default=4)
    cycles = models.IntegerField(default=50)
    preruncycles = models.IntegerField(default=10)
    ConfoundOrder = models.IntegerField(default=3)
    MaxRepeat = models.IntegerField(default=6)
    def __unicode__(self): # Python 3: __str__
        return "<DesignModel:%s>" %self.SID
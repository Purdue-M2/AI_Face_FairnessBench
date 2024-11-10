from utils.registry import LOSSFUNC
from .cross_entropy_loss import CrossEntropyLoss
from .contrastive_regularization import ContrastiveLoss
from .l1_loss import L1Loss
from .bal_loss import LDAMLoss
from .daw_bce_loss import DawBCELoss
from .bce_loss import BCELoss
from .am_softmax import AMSoftmaxLoss
from .consistency_loss import ConsistencyCos
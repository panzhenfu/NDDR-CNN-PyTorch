from yacs.config import CfgNode as CN


_C = CN()

_C.DATA_DIR = 'datasets/nyu_v2'
_C.LOG_DIR = 'run'
_C.SAVE_DIR = 'ckpts'
_C.EXPERIMENT_NAME = 'vgg16_nddr_pret'

_C.CUDA = True
_C.SEED = 1

_C.IGNORE_LABEL = 255

_C.MODEL = CN()

_C.MODEL.SHORTCUT = False
_C.MODEL.NET1_CLASSES = 40
_C.MODEL.NET2_CLASSES = 3


_C.TRAIN = CN()

_C.TRAIN.OUTPUT_SIZE = (321, 321)
_C.TRAIN.DATA_LIST_1 = 'datasets/nyu_v2/list/training_seg.txt'
_C.TRAIN.DATA_LIST_2 = 'datasets/nyu_v2/list/training_normal_mask.txt'

_C.TRAIN.RANDOM_SCALE = True
_C.TRAIN.RANDOM_MIRROR = True
_C.TRAIN.RANDOM_CROP = True

_C.TRAIN.WEIGHT_1 = 'TFDeepLab'
_C.TRAIN.WEIGHT_2 = 'TFDeepLab'

_C.TRAIN.BATCH_SIZE = 10
_C.TRAIN.STEPS = 20001
_C.TRAIN.LR = 0.001
_C.TRAIN.MOMENTUM = 0.9
_C.TRAIN.WEIGHT_DECAY = 2.5e-4
_C.TRAIN.POWER = 0.9
_C.TRAIN.NDDR_FACTOR = 100.
_C.TRAIN.NORMAL_FACTOR = 20.

_C.TRAIN.LOG_INTERVAL = 10
_C.TRAIN.SAVE_INTERVAL = 1000


_C.TEST = CN()

_C.TEST.OUTPUT_SIZE = (-1, -1)
_C.TEST.DATA_LIST_1 = 'datasets/nyu_v2/list/testing_seg.txt'
_C.TEST.DATA_LIST_2 = 'datasets/nyu_v2/list/testing_normal_mask.txt'

_C.TEST.RANDOM_SCALE = False
_C.TEST.RANDOM_MIRROR = False
_C.TEST.RANDOM_CROP = False

_C.TEST.BATCH_SIZE = 10

_C.TEST.LOG_INTERVAL = 10
_C.TEST.SAVE_INTERVAL = 1000
_C.TEST.CKPT_ID = 20000

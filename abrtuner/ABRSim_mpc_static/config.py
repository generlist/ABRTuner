### debug configuration
DEBUG = False
VERBOSE_DEBUG = False
CHUNK_DEBUG = False

### simulation configuration
# MEDIAN_BITRATE_MODE = True
CHUNK_AWARE_MODE = True
PS_STYLE_BANDWIDTH = False
VALIDATION_MODE = False
TOTAL_CHUNKS  = 0
AVERAGE_BANDWIDTH_MODE = False
ESTIMATED_BANDWIDTH_MODE = True
INDUCE_BW_ERROR = False
PRINT_CONFIG_MODE = False
EXPERIMENT_MODE = False


## chunk interunption
NOINTERUPT = True
ALLINTERUPT  = False
SMARTINTERUPT = False

### Operation mode ###
DATABRICKS_MODE = False
TRACE_MODE = True

### BB ABR configuration
conf = {'maxbuflen':120, 'r': 5, 'maxRPct':0.50, 'xLookahead':50}

### Player properties ###
MAX_BUFFLEN = 12000
LOCK = 0

### ABR configuration ###
COMBINATION_ABR = False
UTILITY_BITRATE_SELECTION = False
BANDWIDTH_UTILITY = False
BUFFERLEN_UTILITY = False
BUFFERLEN_BBA1_UTILITY = False
BUFFERLEN_BBA2_UTILITY = False
WEIGHTED_BANDWIDTH = False
MPC_ABR = True
HYB_ABR = False

### COMBINATION ABR settings
COMBINATION_ABR_BW_THRESHOLD = 3000.0
COMBINATION_ABR_CV_THRESHOLD = 1.0

### DYNAMIC settings
DYNAMIC_BSM = False
ONCD = False

### Simulation settings
SIMULATION_STEP = 50

### Video settings
TOTAL_CHUNKS = 49
NUM_BITRATES = 6
VIDEO_BIT_RATE = [300,750,1200,1850,2850,4300]
VIDEO_BIT_RATE_TO_INDEX = {300:0,750:1,1200:2,1850:3,2850:4,4300:5}
REBUF_PENALTY = 4.3 #100000.0#4.3
SMOOTH_PENALTY = 0.0
CHUNKSIZE = 4.0

### MPC settings
WINDOWSIZE = 5

### Output stats settings
TRUE_AVG_BITRATE = False


### racecar video settings
#VIDEO_BIT_RATE = [350,600,1000,2000,3000]
#VIDEO_BIT_RATE_TO_INDEX = {350:0,600:1,1000:2,2000:3,3000:4}
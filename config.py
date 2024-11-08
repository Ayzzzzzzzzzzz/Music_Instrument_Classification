class CreateDataset:
    # Name of dataset csv
    Name = 'dataset.csv'
    # Train Path
    data_path = './philharmonia/'
    train_path = './philharmonia/train/'
    test_path = './philharmonia/test/'
    # Sampling rate
    sr = 22050
    # Frame size (samples)
    fs = 2048
    # Hop size (samples)
    hs = 512
    # MFCC
    mfcc_dim = 13
    # Number of Chorma Coefficients
    cs = 12
    # Mel-scale Coefficient
    ms = 10
    # Tonal Centroid Size
    ts = 6
    # Name of Instrument
    Instrument = ['banjo', 'bass clarinet', 'bassoon', 'cello', 'clarinet', 
                  'contrabassoon', 'cor anglais', 'double bass', 'flute', 
                  'french horn', 'guitar', 'mandolin', 'oboe', 'percussion',
                  'saxophone', 'trombone', 'trumpet', 'tuba', 'viola', 'violin']
    # Label map
    label_map = {
        'banjo': 1,
        'bass clarinet': 2,
        'bassoon': 3,
        'cello': 4,
        'clarinet': 5,
        'contrabassoon': 6,
        'cor anglais': 7,
        'double bass': 8,
        'flute': 9,
        'french horn': 10,
        'guitar': 11,
        'mandolin': 12,
        'oboe': 13,
        'percussion': 14,
        'saxophone': 15,
        'trombone': 16,
        'trumpet': 17,
        'tuba': 18,
        'viola': 19,
        'violin': 20
    }

    Feature_Names = ['meanSpecCentroid', 'stdSpecCentroid',
                     'meanSpecBandwidth', 'stdSpecBandwidth',
                     'meanSpecContrast', 'stdSpecContrast',
                     'meanSpecRollof', 'stdSpecRollof',
                     'meanSpecFlux', 'stdSpecFlux',
                     'meanZCR', 'stdZCR',
                     'meanTempo', 'stdTempo',
                     'meanMFCC_01', 'stdMFCC_01',
                     'meanMFCC_02', 'stdMFCC_02',
                     'meanMFCC_03', 'stdMFCC_03',
                     'meanMFCC_04', 'stdMFCC_04',
                     'meanMFCC_05', 'stdMFCC_05',
                     'meanMFCC_06', 'stdMFCC_06',
                     'meanMFCC_07', 'stdMFCC_07',
                     'meanMFCC_08', 'stdMFCC_08',
                     'meanMFCC_09', 'stdMFCC_09',
                     'meanMFCC_10', 'stdMFCC_10',
                     'meanMFCC_11', 'stdMFCC_11',
                     'meanMFCC_12', 'stdMFCC_12',
                     'meanMFCC_13', 'stdMFCC_13',
                     'meanChromaSTFT_01', 'stdChromaSTFT_01',
                     'meanChromaSTFT_02', 'stdChromaSTFT_02',
                     'meanChromaSTFT_03', 'stdChromaSTFT_03',
                     'meanChromaSTFT_04', 'stdChromaSTFT_04',
                     'meanChromaSTFT_05', 'stdChromaSTFT_05',
                     'meanChromaSTFT_06', 'stdChromaSTFT_06',
                     'meanChromaSTFT_07', 'stdChromaSTFT_07',
                     'meanChromaSTFT_08', 'stdChromaSTFT_08',
                     'meanChromaSTFT_09', 'stdChromaSTFT_09',
                     'meanChromaSTFT_10', 'stdChromaSTFT_10',
                     'meanChromaSTFT_11', 'stdChromaSTFT_11',
                     'meanChromaSTFT_12', 'stdChromaSTFT_12',
                     'meanMelScale_01', 'stdMelScale_01',
                     'meanMelScale_02', 'stdMelScale_02',
                     'meanMelScale_03', 'stdMelScale03',
                     'meanMelScale_04', 'stdMelScale_04',
                     'meanMelScale_05', 'stdMelScale_05',
                     'meanMelScale_06', 'stdMelScale_06',
                     'meanMelScale_07', 'stdMelScale_07',
                     'meanMelScale_08', 'stdMelScale_08',
                     'meanMelScale_09', 'stdMelScale_09',
                     'meanMelScale_10', 'stdMelScale_10',
                     'meanTonnetz_01', 'stdTonnetz_01',
                     'meanTonnetz_02', 'stdTonnetz_02',
                     'meanTonnetz_03', 'stdTonnetz_03',
                     'meanTonnetz_04', 'stdTonnetz_04',
                     'meanTonnetz_05', 'stdTonnetz_05',
                     'meanTonnetz_06', 'stdTonnetz_06'
                     ]

class Test_path:
    # Path for Test Files
    data_path = './philharmonia/test'


class Model:
    # Name of Model
    NAME = 'model.pkl'

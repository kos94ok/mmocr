dataset_type = 'IcdarDataset'
data_root = 'data/icdar2015'

train = dict(
    type=dataset_type,
    ann_file=f'{data_root}/instances_training-2.json',
    img_prefix=f'{data_root}/train',
    pipeline=None)

test = dict(
    type=dataset_type,
    ann_file=f'{data_root}/instances_validation.json',
    img_prefix=f'{data_root}/validation',
    pipeline=None)

train_list = [train]

test_list = [test]

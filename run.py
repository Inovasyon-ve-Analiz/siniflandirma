from functions import run

#HYPERPARAMETERS            

lr = 1e-4
wd = 0
number_of_epoch = 20
train_dir = "new_dataset/train/PNG"
test_dir = "new_dataset/test/PNG"
save_path = "snapshots"
batch_size = 4
binary_classification = True

run(lr=lr, wd=wd, number_of_epoch=number_of_epoch, train_dir=train_dir, test_dir=test_dir,save_path=save_path, batch_size=batch_size, binary_classification=binary_classification)
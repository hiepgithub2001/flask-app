class HyperParameters:
    def __init__(self, batch_size=64, test_batch_size=100, epochs=10, lr=0.01, gamma=0.5, no_cuda=False, no_mps=False, seed=1, log_interval=10, save_model=False, dry_run=False):
        self.batch_size = batch_size
        self.test_batch_size = test_batch_size
        self.epochs = epochs
        self.lr = lr
        self.gamma = gamma
        self.no_cuda = no_cuda
        self.no_mps = no_mps
        self.seed = seed
        self.log_interval = log_interval
        self.save_model = save_model
        self.dry_run = dry_run
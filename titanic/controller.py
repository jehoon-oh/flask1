from titanic.model import TitanicModel

class TitanicController:
    def __init__(self):
        self._m = TitanicModel()
        self._context = '/Temp/'
        self._train = self.create_train()

    def create_train(self) -> object:
        m = self._m
        m.context = self._context

        m.fname = 'train.csv'
        t1 = m.new_dframe()
        print('-------------train head & columns-------------')
        print(t1.head())
        print(t1.columns)

        m.fname = 'test.csv'
        t2 = m.new_dframe()
        print('-------------test head & columns---------------')
        print(t2.head())
        print(t2.columns)

        print('-------------hook 메소드 시작---------------')
        train = m.hook_process(t1, t2)

        return train

    def create_model(self):
        train = self._train
        model = train.drop('Survived', axis = 1)
        print('-----------Model Info------------')
        print(model.info)
        return model

    def create_dummy(self):
        train = self._train
        dummy = train['Survived']
        return dummy

    @staticmethod
    def create_random_variables(train, X_feature, Y_feature)->[]:
        pass
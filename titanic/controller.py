from titanic.model import TitanicModel
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.svm import SVC
import pandas as pd

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

    def test_all(self):
        model = self.create_model()
        dummy = self.create_dummy()
        m = self._m
        m.hook_test(model, dummy)

    def submit(self):
        m = self._m
        model = self.create_model()
        dummy = self.create_dummy()
        test = m.test
        test_id = m.test_id

        clf = SVC()
        clf.fit(model, dummy)
        prediction = clf.predict(test)
        submission = pd.DataFrame(
            {'PassengerId' : test_id, 'Survived' : prediction})
        print(submission.head())
        submission.to_csv(m.context+'submission.csv', index=False)
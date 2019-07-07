from naivebayes_dog_cat.word_frequence import WordFrequence
from naivebayes_dog_cat.naivebayes_naver_movie import NaiveBayesClassfier

if __name__ == '__main__':
    #w = WordFrequence()
    #w.execute()

    context = './data/'
    model = NaiveBayesClassfier()
    model.train(context + 'review_train.csv')
    print(model.classfy('내 인생 최고의 영화'))
    print(model.classfy('내 인생에서 쓰레기같은 영화'))
    print(model.classfy('그저 그러네'))
    print(model.classfy('그냥 시간 때우기'))
    print(model.classfy('완존 재밌어요'))
import csv


class RawMovieReview:
    def __init__(self, file_name='samples.csv'):
        fd = open(file_name, 'r')

        f = csv.reader(fd, delimiter=',')
        self._data = []
        for i in f:
            break
        for i in f:
            self._data.append(i)
        
    
    def __getitem__(self, index):
        return tuple(self._data[index])

    def __len__(self):
        return len(self._data)

class MovieReview(RawMovieReview):
    def __init__(self, score_threshold):
        super().__init__()
        self.threshold = score_threshold

    def __getitem__(self, index):
        if int(self._data[index][2]) >= self.threshold:
            re = True
        else:
            re = False
        review = self._data[index][1]
        
        return tuple([review.strip(" "), re])
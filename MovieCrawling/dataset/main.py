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
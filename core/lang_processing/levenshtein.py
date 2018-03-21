
class LevenshteinDistance(object):

    def distance(self, word_a, word_b):
        if word_a == '':
            return len(word_b)
        elif word_b == '':
            return len(word_a)

        joint_addition_cost = 0 if word_a[-1] == word_b[-1] else 2

        return min(
            self.distance(word_a[:-1], word_b) + 1,
            self.distance(word_a, word_b[:-1]) + 1,
            self.distance(word_a[:-1], word_b[:-1]) + joint_addition_cost,
        )

class Person(object):
    def __init__(self, family_name, first_name):
        self.family_name = family_name
        self.first_name = first_name

    def familyName(self):
        return self.family_name

    def firstName(self):
        return self.first_name

    def __cmp__(self, other):
        return cmp((self.family_name, self.first_name),
                   (other.family_name, other.first_name))

    def __str__(self):
        return '<Person: %s %s>' % (self.first_name, self.family_name)

    def say(self, to_whom, something):
        return self.first_name + ' ' + self.family_name + ' says to ' + to_whom.firstName() + ' ' + to_whom.familyName() + ': ' + something

    def sing(self, to_whom, something):
        return self.say(to_whom, something + ' tra la la')


class MITPerson(Person):
    nextIdNum = 0

    def __init__(self, family_name, first_name):
        Person.__init__(self, family_name, first_name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def get_id_num(self):
        return self.idNum

    def __str__(self):
        return '<MIT Person: %s %s>' % (self.first_name, self.family_name)

    def __cmp__(self, other):
        return cmp(self.idNum, other.idNum)


class UG(MITPerson):
    def __init__(self, family_name, first_name):
        MITPerson.__init__(self, family_name, first_name)
        self.year = None

    def set_year(self, year):
        if year > 5:
            raise OverflowError('Too many')
        self.year = year

    def get_year(self):
        return self.year

    def say(self, to_whom, something):
        return MITPerson.say(self, to_whom, 'Excuse me, but ' + something)


class Prof(MITPerson):
    def __init__(self, familyName, firstName, rank):

        MITPerson.__init__(self, familyName, firstName)
        self.rank = rank
        self.teaching = {}

    def add_teaching(self, term, subj):

        try:
            self.teaching[term].append(subj)
        except KeyError:
            self.teaching[term] = [subj]

    def get_teaching(self, term):

        try:
            return self.teaching[term]
        except KeyError:
            return None

    def lecture(self, to_whom, something):

        return self.say(to_whom, something + ' as it is obvious')

    def say(self, to_whom, something):

        if type(to_whom) == UG:
            return MITPerson.say(self, to_whom, 'I do not understand why you say ' +
                                 something)
        elif type(to_whom) == Prof:
            return MITPerson.say(self, to_whom, 'I really liked your paper on ' +
                                 something)
        else:
            return self.lecture(something)


class Faculty(object):
    def __init__(self):

        self.names = []
        self.IDs = []
        self.members = []
        self.place = None

    def add(self, who):

        if type(who) != Prof:
            raise TypeError('not a professor')
        if who.get_id_num() in self.IDs:
            raise ValueError('duplicate ID')
        self.names.append(who.familyName())
        self.IDs.append(who.get_id_num())
        self.members.append(who)

    def __iter__(self):

        self.place = 0
        return self

    def next(self):

        if self.place >= len(self.names):
            raise StopIteration
        self.place += 1
        return self.members[self.place - 1]

from math import sqrt


class BaseClass(object):
    '''
    docstring for ClassName
    '''
    def __init__(self, num_subjects):
        self.group1 = {}
        self.group2 = {}
        self.group3 = {}
        self.group4 = {}
        self.group5 = {}
        if num_subjects < 7 or num_subjects > 9:
            raise ValueError('Can not have less than 7 subjects or more than 9')
        self.num_subjects = num_subjects
        self.subjects_left = num_subjects

    def get_weighted_cp(self, raw_cp, aggregate_cp):
        rcp = raw_cp / 48
        acp = aggregate_cp / 84
        wcp = sqrt(rcp * acp) * 48
        wcp = round(wcp, 4)
        return wcp

    def get_raw_cp(self, raw_cp):
        raw_cp = raw_cp.upper()
        if raw_cp == 'A':
            raw_cpoint = 12
        elif raw_cp == 'A-':
            raw_cpoint = 11
        elif raw_cp == 'B+':
            raw_cpoint = 10
        elif raw_cp == 'B':
            raw_cpoint = 9
        elif raw_cp == 'B-':
            raw_cpoint = 8
        elif raw_cp == 'C+':
            raw_cpoint = 7
        elif raw_cp == 'C':
            raw_cpoint = 6
        elif raw_cp == 'C-':
            raw_cpoint = 5
        elif raw_cp == 'D+':
            raw_cpoint = 4
        elif raw_cp == 'D':
            raw_cpoint = 3
        elif raw_cp == 'D-':
            raw_cpoint = 2
        elif raw_cp == 'E':
            raw_cpoint = 1
        else:
            print('That is not a valid input')
            raw_cpoint = None
        return raw_cpoint

    def select_group2(self, selection):
        selection = selection.replace(' ', '')
        selection = selection.split(',')
        selection = list(set(selection))
        subjects = []

        if '1' in selection:
            subjects.append('Biology')
        if '2' in selection:
            subjects.append('Chemistry')
        if '3' in selection:
            subjects.append('Physics')
        if '4' in selection:
            subjects.append('General Science')
        return subjects

    def select_group3(self, selection):
        selection = selection.replace(' ', '')
        selection = selection.split(',')
        selection = list(set(selection))
        subjects = []

        if '1' in selection:
            subjects.append('Christian Religious Education')
        if '2' in selection:
            subjects.append('Geography')
        if '3' in selection:
            subjects.append('Hindu Religious Education')
        if '4' in selection:
            subjects.append('History and Government')
        if '5' in selection:
            subjects.append('Islamic Religious Education')
        return subjects

    def select_group4(self, selection):
        selection = selection.replace(' ', '')
        selection = selection.split(',')
        selection = list(set(selection))
        subjects = []

        if '1' in selection:
            subjects.append('Agriculture')
        if '2' in selection:
            subjects.append('Art and Design')
        if '3' in selection:
            subjects.append('Aviation Technology')
        if '4' in selection:
            subjects.append('Building Construction')
        if '5' in selection:
            subjects.append('Computer Studies')
        if '6' in selection:
            subjects.append('Drawing and Design')
        if '7' in selection:
            subjects.append('Electricity')
        if '8' in selection:
            subjects.append('Home Science')
        if '9' in selection:
            subjects.append('Metalwork')
        if '10' in selection:
            subjects.append('Power Mechanics')
        if '11' in selection:
            subjects.append('Woodwork')
        return subjects

    def select_group5(self, selection):
        selection = selection.replace(' ', '')
        selection = selection.split(',')
        selection = list(set(selection))
        subjects = []

        if '1' in selection:
            subjects.append('Arabic')
        if '2' in selection:
            subjects.append('Business Studies')
        if '3' in selection:
            subjects.append('French')
        if '4' in selection:
            subjects.append('German')
        if '5' in selection:
            subjects.append('Kenya Sign Language')
        if '6' in selection:
            subjects.append('Music')
        return subjects

    def get_g1_grades(self):
        self.group1['English'] = self.get_raw_cp(eng)
        self.group1['Kiswahili'] = self.get_raw_cp(kis)
        self.group1['Mathematics'] = self.get_raw_cp(math)
        subjects_left = int(self.num_subjects) - 3
        self.get_g2_grades(subjects_left)

    def get_g2_grades(self, selection, subjects_left):
        '''

        '''
        g2_subjects = self.select_group2(selection)
        if len(g2_subjects) < 2 or len(g2_subjects) > 3:
            print('You must select 2-3 subjects from this group\n')
            self.get_g2_grades(subjects_left)

        print('You selected: {}. Is this correct?'.format(
            ', '.join(g2_subjects)))
        yes_no = input()
        if yes_no == 'N':
            self.get_g2_grades(subjects_left)

        for subject in g2_subjects:
            grade = input('Enter your {} grade: '.format(subject))
            self.group2[subject] = grade.upper()
        print('You got:')
        for subject in self.group2:
            print('{} in {}'.format(self.group2[subject], subject))
        print('Is this correct?')
        yes_no = input()
        if yes_no == 'N':
            self.get_g2_grades(subjects_left)

        for subject in self.group2:
            self.group2[subject] = self.get_raw_cp(self.group2[subject])

        subjects_left = subjects_left - len(g2_subjects)
        if subjects_left > 0:
            self.get_g3_grades(subjects_left)

    def get_g3_grades(self, subjects_left):
        print('Select your Group 3 subjects:\n'
              '1 Christian Religious Education\n'
              '2 Geography\n'
              '3 Hindu Religious Education\n'
              '4 History and Government\n'
              '5 Islamic Religious Education\n')
        g3_subjects = input()
        g3_subjects = self.select_group3(g3_subjects)

        if len(g3_subjects) > subjects_left:
            print('You can not select more than {} subjects from this group'.
                  format(subjects_left))
            self.get_g3_grades(subjects_left)

        print('You selected: {}. Is this correct?'.format(
            ', '.join(g3_subjects)))
        yes_no = input()
        if yes_no == 'N':
            self.get_g3_grades(subjects_left)

        for subject in g3_subjects:
            grade = input('Enter your {} grade: '.format(subject))
            self.group3[subject] = grade.upper()
        print('You got:')
        for key in self.group3:
            print('{} in {}'.format(self.group3[key], key))
        print('Is this correct?')
        yes_no = input()
        if yes_no == 'N':
            self.get_g3_grades(subjects_left)

        for subject in self.group3:
            self.group3[subject] = self.get_raw_cp(self.group3[subject])

        subjects_left = subjects_left - len(g3_subjects)
        if subjects_left > 0:
            self.get_g4_grades(subjects_left)

    def get_g4_grades(self, subjects_left):
        print('Did you do any of these group 4 subjects?\n'
              'Agriculture\n'
              'Art and Design\n'
              'Aviation Technology\n'
              'Building Construction\n'
              'Computer Studies\n'
              'Drawing and Design\n'
              'Electricity\n'
              'Home Science\n'
              'Metalwork\n'
              'Power Mechanics\n'
              'Woodwork\n')
        yes_no = input()
        if yes_no == 'N':
            self.get_g5_grades(subjects_left)
            return

        print('Select your Group 4 subjects:\n'
              '1 Agriculture\n'
              '2 Art and Design\n'
              '3 Aviation Technology\n'
              '4 Building Construction\n'
              '5 Computer Studies\n'
              '6 Drawing and Design\n'
              '7 Electricity\n'
              '8 Home Science\n'
              '9 Metalwork\n'
              '10 Power Mechanics\n'
              '11 Woodwork\n')
        g4_subjects = input()
        g4_subjects = self.select_group4(g4_subjects)

        if len(g4_subjects) > subjects_left:
            print('You can not select more than {} subjects from this group'.
                  format(subjects_left))
            self.get_g4_grades(subjects_left)

        print('You selected: {}. Is this correct?'.format(
            ', '.join(g4_subjects)))
        yes_no = input()
        if yes_no == 'N':
            self.get_g4_grades(subjects_left)

        for subject in g4_subjects:
            grade = input('Enter your {} grade: '.format(subject))
            self.group4[subject] = grade.upper()
        print('You got:')
        for key in self.group4:
            print('{} in {}'.format(self.group4[key], key))
        print('Is this correct?')
        yes_no = input()
        if yes_no == 'N':
            self.get_g4_grades(subjects_left)

        for subject in self.group4:
            self.group4[subject] = self.get_raw_cp(self.group4[subject])

        subjects_left = subjects_left - len(g4_subjects)
        if subjects_left > 0:
            self.get_g5_grades(subjects_left)

    def get_g5_grades(self, subjects_left):
        print('Select your Group 5 subjects:\n'
              '1 Arabic\n'
              '2 Business Studies\n'
              '3 French\n'
              '4 German\n'
              '5 Kenya Sign Language\n'
              '6 Music\n')
        g5_subjects = input()
        g5_subjects = self.select_group5(g5_subjects)

        if len(g5_subjects) > subjects_left:
            print('You can not select more than {} subjects from this group'.
                  format(subjects_left))
            self.get_g5_grades(subjects_left)

        print('You selected: {}. Is this correct?'.format(
            ', '.join(g5_subjects)))
        yes_no = input()
        if yes_no == 'N':
            self.get_g5_grades(subjects_left)

        for subject in g5_subjects:
            grade = input('Enter your {} grade: '.format(subject))
            self.group5[subject] = grade.upper()
        print('You got:')
        for key in self.group5:
            print('{} in {}'.format(self.group5[key], key))
        print('Is this correct?')
        yes_no = input()
        if yes_no == 'N':
            self.get_g5_grades(subjects_left)

        for subject in self.group5:
            self.group5[subject] = self.get_raw_cp(self.group5[subject])

    def cluster1(self):
        eng = self.group1['English']
        kis = self.group1['Kiswahili']
        math = self.group1['Mathematics']
        group2 = list(self.group2.values())
        group2.sort()
        group3 = list(self.group3.values())
        group3.sort()

        subject1 = eng

        if math > group2[-1]:
            subject2 = math
        else:
            subject2 = group2.pop()

        subject3 = group3.pop()

        combined = group2 + group3
        combined.append(kis)

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        if bool(self.group5):
            group5 = list(self.group5.values())
            combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster2(self):
        eng = self.group1['English']
        kis = self.group1['Kiswahili']
        math = self.group1['Mathematics']
        group2 = list(self.group2.values())
        group2.sort()
        group3 = list(self.group3.values())
        group3.sort()

        if eng > kis:
            subject1 = eng
        else:
            subject1 = kis

        subject2 = math

        if group2[-1] > group3[-1]:
            subject3 = group2.pop()
        else:
            subject3 = group3.pop()

        combined = group2 + group3

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        if bool(self.group5):
            group5 = list(self.group5.values())
            combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster3(self):
        eng = self.group1['English']
        kis = self.group1['Kiswahili']
        math = self.group1['Mathematics']
        group2 = list(self.group2.values())
        group2.sort()
        group3 = list(self.group3.values())
        group3.sort()

        if eng > kis:
            subject1 = eng
        else:
            subject1 = kis

        if math > group2[-1]:
            subject2 = math
        else:
            subject2 = group2.pop()

        subject3 = group3.pop()

        combined = group2 + group3

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        if bool(self.group5):
            group5 = list(self.group5.values())
            combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster4(self):
        math = self.group1['Mathematics']
        group2 = self.group2
        group3 = self.group3

        subject1 = math
        print(self.group2)
        if 'Physics' in group2:
            subject2 = group2['Physics']
            del group2['Physics']
            group2 = list(group2.values())
            group2.sort()
        else:
            return
        print(self.group2)
        if 'Geography' in group3 and group3['Geography'] > group2[-1]:
            subject3 = group3['Geography']
            del group3['Geography']
            group3 = list(group3.values())
            group3.sort()
        else:
            subject3 = group2.pop()
            group3 = list(group3.values())
            group3.sort()

        combined = group2 + group3

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        if bool(self.group5):
            group5 = list(self.group5.values())
            combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4
        return score

    def cluster5(self):
        eng = self.group1['English']
        kis = self.group1['Kiswahili']
        math = self.group1['Mathematics']
        group2 = self.group2
        group3 = list(self.group3.values())
        group3.sort()

        if eng > kis:
            subject1 = eng
        else:
            subject1 = kis

        if 'Biology' in group2 and group2['Biology'] > group2['General Science']:
            subject2 = group2['Biology']
            del group2['Biology']
            group2 = list(group2.values())
            group2.sort()
        elif 'General Science' in group2:
            subject2 = group2['General Science']
            del group2['General Science']
            group2 = list(group2.values())
            group2.sort()
        else:
            return

        subject3 = group3.pop()

        combined = group2 + group3
        combined.append(math)

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        if bool(self.group5):
            group5 = list(self.group5.values())
            combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster6(self):
        eng = self.group1['English']
        kis = self.group1['Kiswahili']
        math = self.group1['Mathematics']
        group2 = list(self.group2.values())
        group2.sort()
        group3 = list(self.group3.values())
        group3.sort()

        subject1 = kis

        if eng > math:
            subject2 = eng
        else:
            subject2 = math

        subject3 = group3.pop()

        combined = group2 + group3

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        if bool(self.group5):
            group5 = list(self.group5.values())
            combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster7(self):
        math = self.group1['Mathematics']
        group2 = self.group2
        group3 = list(self.group3.values())
        group3.sort()

        subject1 = math

        if 'Physics' in group2:
            subject2 = group2['Physics']
            del group2['Physics']
        else:
            return

        if 'Chemistry' in group2:
            subject3 = group2['Chemistry']
            del group2['Chemistry']
        else:
            return

        if 'Biology' in group2:
            bio = group2['Biology']

        combined = []
        combined.append(bio)
        combined += group3

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        if bool(self.group5):
            group5 = list(self.group5.values())
            combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster8(self):
        math = self.group1['Mathematics']
        group2 = self.group2
        group3 = list(self.group3.values())
        group3.sort()

        subject1 = math

        if 'Physics' in group2:
            subject2 = group2['Physics']
            del group2['Physics']
            group2 = list(group2.values())
            group2.sort()
        else:
            return

        subject3 = group3.pop()

        combined = group2 + group3

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        if bool(self.group5):
            group5 = list(self.group5.values())
            combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster9(self):
        math = self.group1['Mathematics']
        group2 = self.group2
        group3 = list(self.group3.values())
        group3.sort()

        subject1 = math

        if 'Physics' in group2:
            subject2 = group2['Physics']
            del group2['Physics']
            group2 = list(group2.values())
            group2.sort()
        else:
            return

        if group2[-1] > group3[-1]:
            subject3 = group2.pop()
        else:
            subject3 = group3.pop()

        combined = group2 + group3

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        if bool(self.group5):
            group5 = list(self.group5.values())
            combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster10(self):
        math = self.group1['Mathematics']
        group2 = self.group2
        group3 = list(self.group3.values())
        group3.sort()
        subject1 = math

        if 'Biology' in group2:
            subject2 = group2['Biology']
            del group2['Biology']
        else:
            return

        if 'Chemistry' in group2 and 'Physics' in group2:
            if group2['Chemistry'] > group2['Physics']:
                subject3 = group2['Chemistry']
                del group2['Chemistry']
                group2 = list(group2.values())
                group2.sort()
            else:
                subject3 = group2['Physics']
                del group2['Physics']
                group2 = list(group2.values())
                group2.sort()
        elif 'Chemistry' in group2 and 'Physics' not in group2:
            subject3 = group2['Chemistry']
            del group2['Chemistry']
            group2 = list(group2.values())
            group2.sort()
        elif 'Physics' in group2 and 'Chemistry' not in group2:
            subject3 = group2['Physics']
            del group2['Physics']
            group2 = list(group2.values())
            group2.sort()
        else:
            return

        combined = group2 + group3

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        if bool(self.group5):
            group5 = list(self.group5.values())
            combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster11(self):
        math = self.group1['Mathematics']
        group2 = list(self.group2.values())
        group2.sort()
        group3 = list(self.group3.values())
        group3.sort()

        subject1 = math
        subject2 = group2.pop()

        subject3 = group2.pop()

        combined = group2 + group3

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        if bool(self.group5):
            group5 = list(self.group5.values())
            combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster12(self):
        math = self.group1['Mathematics']
        group2 = list(self.group2.values())
        group2.sort()
        group3 = list(self.group3.values())
        group3.sort()

        subject1 = math

        subject2 = group2.pop()

        subject3 = group3.pop()

        combined = group2 + group3

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        if bool(self.group5):
            group5 = list(self.group5.values())
            combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster13(self):
        eng = self.group1['English']
        kis = self.group1['Kiswahili']
        math = self.group1['Mathematics']
        group2 = self.group2
        group3 = list(self.group3.values())
        group3.sort()
        if bool(self.group4):
            group4 = self.group4

        if 'Chemistry' in group2:
            subject1 = group2['Chemistry']
            del group2['Chemistry']
        else:
            return

        if 'Physics' in group2 and 'Home ' > math:
            subject2 = group2['Physics']
            del group2['Physics']
        else:
            subject2 = math

        if 'Biology' in group2 and 'Home Science' in group4:
            if group2['Biology'] > group4['Home Science']:
                subject3 = group2['Biology']
                del group2['Biology']
                group2 = list(group2.values())
                group2.sort()
                group4 = list(group4.values())
                group4.sort()
            else:
                subject3 = group4['Home Science']
                del group4['Home Science']
                group4 = list(group4.values())
                group4.sort()
                group2 = list(group2.values())
                group2.sort()
        elif 'Biology' in group2 and 'Home Science' not in group4:
            subject3 = group2['Biology']
            del group2['Biology']
            group2 = list(group2.values())
            group2.sort()
            if bool(group4):
                group4 = list(group4.values())
                group4.sort()
        elif 'Biology' not in group2 and 'Home Science' in group4:
            subject3 = group4['Home Science']
            del group4['Home Science']
            group4 = list(group4.values())
            group4.sort()
            group2 = list(group2.values())
            group2.sort()
        else:
            return

        combined = group2 + group3
        combined.append(eng)
        combined.append(kis)

        if bool(group4):
            combined += group4
        if bool(self.group5):
            group5 = list(self.group5.values())
            combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster14(self):
        eng = self.group1['English']
        kis = self.group1['Kiswahili']
        math = self.group1['Mathematics']
        group2 = self.group2.values()
        group3 = list(self.group3.values())
        group3.sort()

        if 'Biology' in group2 and 'General Science' in group2:
            if group2['Biology'] > group2['General Science']:
                subject1 = group2['Biology']
                del group2['Biology']
                group2 = list(group2.values())
                group2.sort()
            else:
                subject1 = group2['General Science']
                del group2['General Science']
                group2 = list(group2.values())
                group2.sort()
        elif 'Biology' in group2 and 'General Science' not in group2:
            subject1 = group2['Biology']
            del group2['Biology']
            group2 = list(group2.values())
            group2.sort()
        elif 'Biology' not in group2 and 'General Science' in group2:
            subject1 = group2['General Science']
            del group2['General Science']
            group2 = list(group2.values())
            group2.sort()
        else:
            return

        subject2 = math

        if group2[-1] > group3[-1]:
            subject3 = group2.pop()
        else:
            subject3 = group3.pop()

        combined = group2 + group3
        combined.append(kis)
        combined.append(eng)

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        if bool(self.group5):
            group5 = list(self.group5.values())
            combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster15(self):
        eng = self.group1['English']
        kis = self.group1['Kiswahili']
        math = self.group1['Mathematics']
        group2 = self.group2
        group3 = list(self.group3.values())
        group3.sort()

        if 'Biology' in group2:
            subject1 = group2['Biology']
            del group2['Biology']
        else:
            return

        if 'Chemistry' in group2:
            subject2 = group2['Chemistry']
            del group2['Chemistry']
        else:
            return

        if 'Physics' in group2 and group2['Physics'] > math:
            subject3 = group2['Physics']
            del group2['Physics']
        else:
            subject3 = math

        group2 = list(group2.values())
        group2.sort()

        combined = group2 + group3
        combined.append(eng)
        combined.append(kis)

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        if bool(self.group5):
            group5 = list(self.group5.values())
            combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster16(self):
        eng = self.group1['English']
        kis = self.group1['Kiswahili']
        math = self.group1['Mathematics']
        group2 = list(self.group2)
        group2.sort()
        group3 = list(self.group3.values())
        group3.sort()

        if 'History and Government' in group3:
            subject1 = group3['History and Government']
            del group3['History and Government']
            group3 = list(group2.values())
            group3.sort()
        else:
            return

        if eng > kis:
            subject2 = eng
        else:
            subject2 = kis

        if math > group2[-1]:
            subject3 = math
        else:
            subject3 = group2.pop()

        combined = group2 + group3

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        if bool(self.group5):
            group5 = list(self.group5.values())
            combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster17(self):
        eng = self.group1['English']
        kis = self.group1['Kiswahili']
        math = self.group1['Mathematics']
        group2 = self.group2
        group3 = list(self.group3.values())
        group3.sort()

        if 'Biology' in group2:
            subject1 = group2['Biology']
            del group2['Biology']
        else:
            return

        if 'Chemistry' in group2:
            subject2 = group2['Chemistry']
            del group2['Chemistry']
        else:
            return

        if 'Biology' in group2 and 'Physics' in group2:
            if group2['Physics'] > math and group2['Physics'] > group2['Biology']:
                subject3 = group2['Physics']
                del group2['Physics']
            elif group2['Biology'] > math:
                subject3 = group2['Biology']
                del group2['Biology']
            else:
                subject3 = math
        elif 'Biology' in group2 and 'Physics' not in group2:
            if group2['Biology'] > math:
                subject3 = group2['Biology']
                del group2['Biology']
            else:
                subject3 = math
        elif 'Biology' not in group2 and 'Physics' in group2:
            if group2['Physics'] > math:
                subject3 = group2['Physics']
                del group2['Physics']
            else:
                subject3 = math

        group2 = list(group2.values())
        group2.sort()

        combined = group2 + group3
        combined.append(eng)
        combined.append(kis)

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        if bool(self.group5):
            group5 = list(self.group5.values())
            combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster18(self):
        eng = self.group1['English']
        kis = self.group1['Kiswahili']
        math = self.group1['Mathematics']
        group2 = list(self.group2.values())
        group2.sort()
        group3 = self.group3

        if 'Geography' in group3:
            subject1 = group3['Geography']
            del group3['Geography']
            group3 = list(group3.values())
            group3.sort()
        else:
            return

        subject2 = math

        subject3 = group2.pop()

        combined = group2 + group3

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        if bool(self.group5):
            group5 = list(self.group5.values())
            combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster19(self):
        eng = self.group1['English']
        kis = self.group1['Kiswahili']
        math = self.group1['Mathematics']
        group2 = list(self.group2)
        group2.sort()
        group3 = list(self.group3.values())
        group3.sort()
        if bool(self.group5):
            group5 = self.group5
        else:
            return

        if 'French' in group5:
            subject1 = group5['French']
            del group5['French']
            group5 = list(group5.values())
            group5.sort()
        else:
            return

        if eng > kis:
            subject2 = eng
        else:
            subject2 = kis

        if group2[-1] > group3[-1] and group2[-1] > math:
            subject3 = group2.pop()
        elif group3[-1] > math:
            subject3 = group3.pop()
        else:
            subject3 = math

        combined = group2 + group3

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster20(self):
        eng = self.group1['English']
        kis = self.group1['Kiswahili']
        math = self.group1['Mathematics']
        group2 = list(self.group2)
        group2.sort()
        group3 = list(self.group3.values())
        group3.sort()
        if bool(self.group5):
            group5 = self.group5
        else:
            return

        if 'German' in group5:
            subject1 = group5['German']
            del group5['German']
            group5 = list(group5.values())
            group5.sort()
        else:
            return

        if eng > kis:
            subject2 = eng
        else:
            subject2 = kis

        if group2[-1] > group3[-1] and group2[-1] > math:
            subject3 = group2.pop()
        elif group3[-1] > math:
            subject3 = group3.pop()
        else:
            subject3 = math

        combined = group2 + group3

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

    def cluster21(self):
        eng = self.group1['English']
        kis = self.group1['Kiswahili']
        math = self.group1['Mathematics']
        group2 = list(self.group2)
        group2.sort()
        group3 = list(self.group3.values())
        group3.sort()
        if bool(self.group5):
            group5 = self.group5
        else:
            return

        if 'Music' in group5:
            subject1 = group5['Music']
            del group5['Music']
            group5 = list(group5.values())
            group5.sort()
        else:
            return

        if eng > kis:
            subject2 = eng
        else:
            subject2 = kis

        if group2[-1] > group3[-1] and group2[-1] > math:
            subject3 = group2.pop()
        elif group3[-1] > math:
            subject3 = group3.pop()
        else:
            subject3 = math

        combined = group2 + group3

        if bool(self.group4):
            group4 = list(self.group4.values())
            combined += group4
        combined += group5

        combined.sort()

        subject4 = combined.pop()

        score = subject1 + subject2 + subject3 + subject4

        return score

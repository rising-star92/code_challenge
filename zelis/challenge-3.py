#####################################################################################
############################ Challenge 3 ############################################
#####################################################################################

words = ["albums", "barely", "befoul", "convex", "hereby", "jigsaw", "tailor", "weaver"]

pieces = ["al", "bums", "bar", "ely", "be", "foul", "con", "vex", "here", "by", "jig", "saw", "tail", "or", "we", "aver"]

def findletters(words, pieces):
    for w in words:
        for i in range(len(pieces)):
            for j in range(i+1, len(pieces)):
                if w == pieces[i] + pieces[j]:
                    print("{} + {} => {}".format(pieces[i], pieces[j], w))
                else:
                    print("{} != {}".format(pieces[i]+pieces[j], w))


findletters(words, pieces)
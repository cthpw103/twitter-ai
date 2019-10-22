import sys
import textgenrnn
import twitter

#asks for api stuff
conkey = input("Consumer key? ")
consec = input("Consumer secret? ")
accesstok = input("Access token? ")
accesstoksec = input("Access token secret? ")
manifest = twitter.api(conkey, consec, accesstok, accesstoksec)

# get tl
cnt = sys.argv[1]
sn = sys.argv[2]
tl = manifest.getUserTimeline(screen_name=sn, count=cnt)

# count and screen names are arguments
tl = get_tweets(api=manifest, screen_name=sn)
reo = open('tweetraw.txt', 'w')
reo.write(tl)
rnn = textgenrnn()

# train from tweets
rnn.train_from_file('tweetraw.txt')

#generate with 3 layers
layers = input("How many layers? ")
geno = rnn.generate(layers, temperature=1.0)

# post ai
final = manifest.PostUpdate(geno)
print(final.text)

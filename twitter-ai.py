import sys
import textgenrnn
import twitter
conkey = input("consumer key?")
consec = input("consumer secret?")
accesstok = input ("access token?")
accesstoksec = input("access token secret?")
manifest = twitter.api(conkey, consec, accesstok, accesstoksec)
tl = manifest.getUserTimeline(screen_name=sn, count=cnt)
cnt = sys.argv[1]
sn = sys.argv[2]
tl = get_tweets(api=manifest, screen_name=sn)
reo = open('tweetraw.txt', 'w')
reo.write(tl)
rnn = textgenrnn()
rnn.train_from_file('tweetraw.txt')
geno = textgen.generate(3, temperature=1.0)
final = manifest.PostUpdate(geno)
print(final.text)

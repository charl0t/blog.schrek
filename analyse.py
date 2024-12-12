# https://github.com/yannbanas/mrkdwn_analysis

from mrkdwn_analysis import MarkdownAnalyzer
import  os


for dirpath, dirs, files in os.walk('content/posts/*'): 
  for filename in files:
    fname = os.path.join(dirpath,filename)
    if fname.endswith('.md'):
      analyzer = MarkdownAnalyzer(fname)
      analysis = analyzer.count_words()
      print(fname)
      print(analysis)



	

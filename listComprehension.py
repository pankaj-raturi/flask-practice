#!/usr/bin/env python3


friends = ['Rolf', 'Sam', 'Samantha', 'Saurabh', 'Jen']
starts_s = [ friend for friend in friends if friend.startswith('S') ]

# starts_s = []
# for friend in friends:
#     if( friend.startswith('S')):
#         starts_s.append(friend)

print(starts_s)
# HiddenRhythms

DP group recommendation algorithm for MIT 6.5610:

Before running any tests, run the following command in Terminal:
`export PYTHONPATH=abs/path/to/hidden-rhythms/`

## Algorithm

Given a group and vectorized samples of each member's preffered song, this algorithm will output a list of songs that take into account everyone's preferences while not revealing any individual user's preferences. Check out [this article on DP](https://google.com) for more information.

## Security Goals

- Prevent users from recovering preferences/tastes for any other user in the group.
- Prevent users from determining whether a taste has been added for noise contribution.

## Adversary Power

- Can see outputted songs
- Can access song database
- Knows the algorithm
- Cannot make more playlist with subsets or supersets of the group.




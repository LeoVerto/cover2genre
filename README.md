# Cover2Genre
You shouldn't judge a book by its cover but what about music? Can we build a system that is capable of making
a somewhat accurate guess about a music album's genre by only looking at the cover art?

## Data pre-processing
1. Download [2018 AcousticBrainz Genre Task][1] dataset
2. Extract unique release group IDs and respective genres, discard subgenres
3. Download 250x250px front cover art from [Cover Art Archive][2] when available
4. Generate dataset


[1]: https://multimediaeval.github.io/2018-AcousticBrainz-Genre-Task/data/
[2]: https://coverartarchive.org/

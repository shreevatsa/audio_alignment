# Raghuvamsha audio <-> text

Aligning the audio from [here](https://archive.org/details/Raghuvamsha-mUlam-vedabhoomi.org) with the text.

## Steps

### Get the audio

Right now, on archive.org, wasn't able to download all the mp3 files together, but was able to download a `.m3u` file containing a list of them:

```sh
curl -L -O https://archive.org/download/Raghuvamsha-mUlam-vedabhoomi.org/Raghuvamsha-mUlam-vedabhoomi.org_vbr.m3u
```

Now can download them all, with:

```sh
wget --input-file=Raghuvamsha-mUlam-vedabhoomi.org_vbr.m3u
rm "00 License CC BY-NC-ND 3.0 Vedabhoomi.mp3"
mkdir audio
mv *.mp3 audio/
mv "Raghuvamsha-mUlam-vedabhoomi.org_vbr.m3u" audio/
```

### Get the text

Where to get the text from? Options:

- GRETIL: [1](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/5_poetry/2_kavya/kragh_pu.htm), [2](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_kAlidAsa-raghuvaMza.htm)
- [sanskritdocuments.org](https://sanskritdocuments.org/sanskrit/kalidasa/), e.g. [sarga1](https://sanskritdocuments.org/doc_z_misc_major_works/raghuvansha1.html)
- [Sanskrit Wikisource](https://sa.wikisource.org/wiki/%E0%A4%B0%E0%A4%98%E0%A5%81%E0%A4%B5%E0%A4%82%E0%A4%B6%E0%A4%AE%E0%A5%8D), e.g. [sarga1](https://sa.wikisource.org/wiki/%E0%A4%B0%E0%A4%98%E0%A5%81%E0%A4%B5%E0%A4%82%E0%A4%B6%E0%A4%AE%E0%A5%8D/%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%A5%E0%A4%AE%E0%A4%83_%E0%A4%B8%E0%A4%B0%E0%A5%8D%E0%A4%97%E0%A4%83)

Let's pick Wikisource so that errors can be corrected.

First attempt: Copy-pasting from https://sa.wikisource.org/wiki/रघुवंशम् into something like Obsidian and editing a bit, gives us the list of urls (in `text.urls`). Then we could try downloading them (`wget --input-file=text.urls`), but that turns out to be a bad idea -- the files are hard to deal with, and the filenames are in alphabetical order ("अष्टादशः सर्गः" comes first). 

Second attempt: We can use [the Wikisource export](https://ws-export.wmcloud.org/?lang=sa&title=%E0%A4%B0%E0%A4%98%E0%A5%81%E0%A4%B5%E0%A4%82%E0%A4%B6%E0%A4%AE%E0%A5%8D) into plain text (downloaded into `raghuvamsha.txt`). Then try to split into files... the problem is that somehow the third sarga appears before the second?

Third attempt: We [can use](https://opendata.stackexchange.com/questions/6974/formats-of-texts-from-wikisource/9431#9431) the `?action=raw` links like [this](https://sa.wikisource.org/wiki/%E0%A4%B0%E0%A4%98%E0%A5%81%E0%A4%B5%E0%A4%82%E0%A4%B6%E0%A4%AE%E0%A5%8D/%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%A5%E0%A4%AE%E0%A4%83_%E0%A4%B8%E0%A4%B0%E0%A5%8D%E0%A4%97%E0%A4%83?action=raw). So back to `text.urls` it is.

```sh
set i 0; for url in (cat text.urls)
    set i (math $i + 1)
    echo $i $url
    curl $url -o $i.txt
    sleep 1
end
```

(Ended up [fixing](https://sa.wikisource.org/w/index.php?title=%E0%A4%B0%E0%A4%98%E0%A5%81%E0%A4%B5%E0%A4%82%E0%A4%B6%E0%A4%AE%E0%A5%8D&diff=404578&oldid=399802) a typo.)

Trying to extract the useful part: turns out, the files on Wikisource are not consistent (half of them don't have `<table>`), but we can filter to lines ending with `</tr></p>`. In Fish (with help from an LLM):

```sh
for file in *.txt
    set useful_output (basename $file .txt)-useful.txt
    set not_useful_output (basename $file .txt)-not-useful.txt

    # Loop through each line of the file
    while read -l line
        if string match -q '*</tr></p>' "$line"
            echo "$line" >> $useful_output
        else
            echo "$line" >> $not_useful_output
        end
    end < $file

    echo "Processed $file: useful lines to $useful_output, not-useful lines to $not_useful_output"
end
```

Do we have the right number of lines? This is what the audio files have (taking the last `.mp3` file for each sarga):

```
Raghuvamsha-Sarga01 95
Raghuvamsha-Sarga02 75
Raghuvamsha-Sarga03 70
Raghuvamsha-Sarga04 88
Raghuvamsha-Sarga05 76
Raghuvamsha-Sarga06 86
Raghuvamsha-Sarga07 71
Raghuvamsha-Sarga08 95
Raghuvamsha-Sarga09 82
Raghuvamsha-Sarga10 86
Raghuvamsha-Sarga11 93
Raghuvamsha-Sarga12 104
Raghuvamsha-Sarga13 79
Raghuvamsha-Sarga14 87
Raghuvamsha-Sarga15 103
Raghuvamsha-Sarga16 88
Raghuvamsha-Sarga17 81
Raghuvamsha-Sarga18 53
Raghuvamsha-Sarga19 57
```

And this is what `wc -l` shows:

```
wc -l *useful.txt
      96 1-useful.txt  > 95 (because of १.३४*)
      76 2-useful.txt  > 75 (because of २.४२*)
      76 3-useful.txt  > 70
      94 4-useful.txt  > 88
      78 5-useful.txt  > 76
      88 6-useful.txt  > 86
      72 7-useful.txt  > 71
     102 8-useful.txt  > 95
      94 9-useful.txt  > 82
      87 10-useful.txt > 86
      96 11-useful.txt > 93
     107 12-useful.txt > 104
      83 13-useful.txt > 79
      87 14-useful.txt = 87
     103 15-useful.txt = 103
      86 16-useful.txt < 88 (16.14 and 16.15 are missing?)
      81 17-useful.txt = 81
      53 18-useful.txt = 53
      57 19-useful.txt = 57
    1616 total
```

Fourth attempt: Let's abandon Wikisource and go back to one of the other sources. Such as https://sanskritsahitya.org/raghuvansham

Verified that the counts of verses match, which is great!

The data is available at https://github.com/sanskritsahitya-com/data

As raw JSON:

```
curl -L -O https://github.com/sanskritsahitya-com/data/raw/refs/heads/main/raghuvansham/raghuvansham.json
jq '.data | map({c, n, i, v})' raghuvansham.json > raghuvamsha.json
```


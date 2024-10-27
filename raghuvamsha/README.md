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
```

### Get the text

Where to get the text from? Options:

- GRETIL: [1](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/5_poetry/2_kavya/kragh_pu.htm), [2](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_kAlidAsa-raghuvaMza.htm)
- [sanskritdocuments.org](https://sanskritdocuments.org/sanskrit/kalidasa/), e.g. [sarga1](https://sanskritdocuments.org/doc_z_misc_major_works/raghuvansha1.html)
- [Sanskrit Wikisource](https://sa.wikisource.org/wiki/%E0%A4%B0%E0%A4%98%E0%A5%81%E0%A4%B5%E0%A4%82%E0%A4%B6%E0%A4%AE%E0%A5%8D), e.g. [sarga1](https://sa.wikisource.org/wiki/%E0%A4%B0%E0%A4%98%E0%A5%81%E0%A4%B5%E0%A4%82%E0%A4%B6%E0%A4%AE%E0%A5%8D/%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%A5%E0%A4%AE%E0%A4%83_%E0%A4%B8%E0%A4%B0%E0%A5%8D%E0%A4%97%E0%A4%83)

Let's pick Wikisource so that errors can be corrected.

Copy-pasting from https://sa.wikisource.org/wiki/रघुवंशम् into Obsidian and editing a bit, gives us the list of urls.


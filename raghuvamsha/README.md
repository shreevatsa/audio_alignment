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


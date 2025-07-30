Script for renaming TV Show Video files named "s{#}e{#}" to "{show name} - s{#}e{#} - {episode name}". Essentially from
the season episode number to the plex format for TV Shows (This does not work for 2 part episodes in the same file but 
those are not the focus)

This is primarily used to help, and is not intended to be a complete-automated solution. I wrote this as a quick solution 
for naming files the appropriate show names since typing all that out is tedious and prone to making mistakes (especially when
renaming dozes or hundreds of episodes)

Example use case (the exact steps I follow): 
1. Rip individual video files from owned physical media using something like MakeMKV 
2. Identify the episode season and number for a file 
3. Rename the file to s{#}e{#}; for example season 1, episode 9 would be s01e09
4. Repeat until all files are named
5. Find the Show and Season on the TVDB; EX: [Show Season Example]( https://www.thetvdb.com/series/avatar-the-last-airbender/seasons/official/1)
6. Use the included extract table JS script in your browser developer console to extract the episode number and name into ~ separated columns. This should produce an output like this: 
```
    "~Name",
    "s01e01~The Boy in the Iceberg",
    "s01e02~The Avatar Returns",
    "s01e03~The Southern Air Temple",
    "s01e04~The Warriors of Kyoshi",
    "s01e05~The King of Omashu",
    "s01e06~Imprisoned",
    "s01e07~The Spirit World: Winter Solstice (1)",
    "s01e08~Avatar Roku: Winter Solstice (2)",
    "s01e09~The Waterbending Scroll",
    "s01e10~Jet",
    "s01e11~The Great Divide",
    "s01e12~The Storm",
    "s01e13~The Blue Spirit\nmid-season finale",
    "s01e14~The Fortuneteller",
    "s01e15~Bato of the Water Tribe",
    "s01e16~The Deserter",
    "s01e17~The Northern Air Temple",
    "s01e18~The Waterbending Master",
    "s01e19~The Siege of the North (1)",
    "s01e20~The Siege of the North (2)\nseason finale"
```
7. Clean up the output by removing anything that is not part of the final file names (exmaple the first ~Name Row, the \nseason finale from the last row, and any " and commas)
8. Result should be something like this
```
    s01e01~The Boy in the Iceberg
    s01e02~The Avatar Returns
    s01e03~The Southern Air Temple
    s01e04~The Warriors of Kyoshi
    s01e05~The King of Omashu
    s01e06~Imprisoned
    s01e07~The Spirit World: Winter Solstice (1)
    s01e08~Avatar Roku: Winter Solstice (2)
    s01e09~The Waterbending Scroll
    s01e10~Jet
    s01e11~The Great Divide
    s01e12~The Storm
    s01e13~The Blue Spirit
    s01e14~The Fortuneteller
    s01e15~Bato of the Water Tribe
    s01e16~The Deserter
    s01e17~The Northern Air Temple
    s01e18~The Waterbending Master
    s01e19~The Siege of the North (1)
    s01e20~The Siege of the North (2)
```
9. Save the output to a file
10. In the Python script, edit the show_name, directory_path, and episode_names_path to be what you need them to be
11. Run the python script
# recast-support
Downloading Meteosat SEVIRI data from 2020-2024 to support the OVERCAST retro run
* requires the epct-desktop conda env
* requires local installation of the HRIT data tailor
* initially set up on jturner@overcast2

To run download: 
1. `conda activate epct-desktop`
2. start data tailor with `epct_webui &>epct.log &`
3. change settings and run `bash seviri_download_parallel.sh`

Saving data to `/mnt/sat/seviri/europe_hrit/`, using format similar to `/mnt/meteosat/` used in YJ's CLAVR-x processing. 

0 deg Meteosat centered over Europe -> EO:EUM:DAT:MSG:HRSEVIRI collection
Indian Ocean Meteosat -> EO:EUM:DAT:MSG:HRSEVIRI-IODC

Documentation for setup:
* [EUMDAC (meteosat data access client)](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)
* [Local Data Tailor](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide#ID-Data-Tailor-Standalone-in-EUMDAC)

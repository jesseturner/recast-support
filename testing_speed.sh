eumdac --verbose download \
    -c EO:EUM:DAT:MSG:HRSEVIRI \
    --product @eumdac_search_results.txt \
    --chain "product: HRSEVIRI, format: hrit" \
    --local-tailor dt_3_2 \
    --output "seviri_sample_hrit/speed_test/"
for day in 2025-06-01 2025-06-02 2025-06-03
do
    mkdir -p "seviri_sample_loop/$day"

    eumdac download \
        -c EO:EUM:DAT:MSG:HRSEVIRI \
        --start ${day}T00:00:00 \
        --end   ${day}T01:00:00 \
        --chain "product: HRSEVIRI, format: hrit" \
        --local-tailor dt_3_2 \
        --output "seviri_sample_loop/$day"
done
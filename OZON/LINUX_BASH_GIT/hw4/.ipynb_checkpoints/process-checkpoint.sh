# #!/bin/bash

# # RATING_AVG=$(
# #     (
# #         in2csv $1 \
# #         | csvsql --query "select AVG(overall_ratingsource) from stdin where overall_ratingsource >= 0" \
# #         | tac \
# #         | sed -n '1p' \
# #     )
# # )

# # echo "RATING_AVG $RATING_AVG"
# # (
# #     in2csv $1 | csvsql --query "select LOWER(country), count(*) from stdin group by LOWER(country)" \
# #               | sed -n '2,$s/^/HOTELNUMBER /p' \
# #               | sed -n 's/,/ /p'
# # )

# # (
# #     in2csv $1 \
# #         | csvsql --query "
# #             select hilton.country, HOLIDAY_INN_CLEANLINESS_AVG, HILTON_CLEANLINESS_AVG from
# #             (
# #                 select LOWER(country) as country, AVG(CLEANLINESS) as HILTON_CLEANLINESS_AVG
# #                 FROM stdin
# #                 WHERE LOWER(doc_id) LIKE '%hilton%'
# #                 GROUP BY LOWER(country)
# #                 ORDER BY LOWER(country)
# #             ) as hilton,
# #             (
# #                 select LOWER(country) as country, AVG(CLEANLINESS) as HOLIDAY_INN_CLEANLINESS_AVG
# #                 FROM stdin
# #                 WHERE LOWER(doc_id) LIKE '%holiday_inn%'
# #                 GROUP BY LOWER(country)
# #                 ORDER BY LOWER(country)
# #             ) as holliday
# #             WHERE holliday.country == hilton.country
# #             " \
# #         | sed -n '2,$s/^/CLEANLINESS /p' \
# #         | sed -n 's/,/ /p' \
# #         | sed -n 's/,/ /p'
# # )


mvvm_filtered_rating_file_name='mvvm_rating_filtered.csv'
gnu_plot_commands='gnu_plot_commands'
# FILE=/etc/resolv.conf
if [[ -f "$mvvm_filtered_rating_file_name" ]]; then
    rm $mvvm_filtered_rating_file_name
fi

if [[ -f "$gnu_plot_commands" ]]; then
    rm $gnu_plot_commands
fi

{
  echo 'set terminal png size 300,400'
  echo "set output 'cleanliness_vs_overall_ratingsource.png'"
  echo 'set datafile separator comma'
  echo 'f(x) = m*x+b '
  echo 'fit f(x) $1 using 12:18 via m,b'
  echo "plot $1 using 12:(\$18>=0?\$18:1/0) title 'cleanliness vs overall_ratingsource' with points, f(x) title 'fit'"
} >> gnu_plot_commands

cat hotels.csv | LC_ALL=C awk -F, '{ if ($18 >= 0) { print } }' > $mvvm_filtered_rating_file_name


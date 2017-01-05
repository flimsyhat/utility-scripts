input_file=$1
margin=$2
output_file=$3

gs -q -sDEVICE=pdfwrite -dBATCH -dNOPAUSE -sOutputFile=$output_file \
  -dDEVICEWIDTHPOINTS=623 -dDEVICEHEIGHTPOINTS=842 -dFIXEDMEDIA \
  -c "<< /CurrPageNum 1 def /Install { /CurrPageNum CurrPageNum 1 add def
   CurrPageNum 2 mod 1 eq {-$margin 0 translate} {$margin 0 translate} ifelse } bind  >> setpagedevice" \
  -f "$input_file"

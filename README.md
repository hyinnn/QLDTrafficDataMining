Instructions for rulemining.py
----------------------------

1. Make sure to have driverdemographics.csv and factorsinroadcrashes.csv in the same folder as rulemining.py

2. Open cmd/terminal and run python rulemining.py

3. Takes 3 arguments 
	i) 	 file: factors / demographics
	ii)  float: min_sup between 0 and 1
	iii) float: min_conf between 0 and 1

	e.g. Mining factorsinroadcrashes.csv with min support as 0.3 and min confidence as  0.5
	cmd/terminal~: python rulemining.py factors 0.3 0.5
#!/bin/bash

# 1. Ensure the verifier directory exists inside the container
mkdir -p /logs/verifier

# 2. Run the pytest suite and generate the CTRF JSON report
pytest --ctrf /logs/verifier/ctrf.json /tests/test_outputs.py -rA

# 3. Check pytest's exit code. If it is 0 (success), write a 1.0 reward.
if [ $? -eq 0 ]; then
    echo "1.0" > /logs/verifier/reward.txt
else
    echo "0.0" > /logs/verifier/reward.txt
fi

exit 0
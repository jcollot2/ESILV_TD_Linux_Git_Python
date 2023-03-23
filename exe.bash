#!/bin/bash

# Value 
value=1036

# Import exo3
imported=$(python3 -c "import exo3; print(exo3.get_manor_ids($value))")
# Set value
echo $imported

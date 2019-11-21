## Installation

1. Install conda
2. Set environment from the root directory

    ` conda env create -f environment.yml `
3. Activate conda

    ` conda activate sisr `
4. Migrate database

    ` python manage.py migrate `
5. Run server (port no is optional - defaults to 8000)

    ` python manage.py runserver  8000`
6. visit http://localhost:8000


## Note

Some changes have been made within the original ML repo to accommodate with the new directory structure. Be careful before updating any thing.
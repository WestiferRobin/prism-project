#!/bin/bash

echo "🛠️ Injecting custom pg_hba.conf..."

cp /custom-config/pg_hba.conf /var/lib/postgresql/data/pg_hba.conf
chown postgres:postgres /var/lib/postgresql/data/pg_hba.conf

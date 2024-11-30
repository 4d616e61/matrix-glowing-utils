sudo -u postgres psql -d synapse -c 'select * from events where room_id = '\'"$1"\'';'

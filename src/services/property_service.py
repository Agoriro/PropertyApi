from typing import List, Dict, Any
from ..models.property import Property
from ..configdb import Database

class PropertyService:
    def __init__(self, database: Database):
        self.database = database

    def get_properties(self, filters: Dict[str, Any]) -> List[Property]:
        query = """
            SELECT
                p.address,
                p.city,
                s.name AS status_name,
                p.price,
                p.description
            FROM
                habi_db.status_history sh
            INNER JOIN
                status s ON sh.status_id = s.id
            INNER JOIN
                property p ON sh.property_id = p.id
            INNER JOIN (
                SELECT
                    sh.property_id,
                    MAX(sh.update_date) AS max_update_date
                FROM
                    habi_db.status_history  sh
				INNER JOIN
					status s ON sh.status_id = s.id
				WHERE s.name in ('pre_venta', 'en_venta','vendido')
                GROUP BY
                    sh.property_id
				
            ) AS latest_status ON sh.property_id = latest_status.property_id
            AND sh.update_date = latest_status.max_update_date
        """
        
        conditions = []
        params = []

        if 'year' in filters and filters['year'] and filters['year'] > 0:
            conditions.append("p.year = %s")
            params.append(filters['year'])
        if 'city' in filters:
            conditions.append("p.city = %s")
            params.append(filters['city'])
        if 'status' in filters:
            conditions.append("s.name = %s")
            params.append(filters['status'])

        if conditions:
            query += " AND " + " AND ".join(conditions)

        print(f"Query {query}")
        print(f"Params {tuple(params)}")
        results = self.database.execute_query(query, tuple(params))
        return [Property(**result) for result in results]
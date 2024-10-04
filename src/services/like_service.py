from typing import List, Optional
from datetime import datetime
from ..models.like import Like
from ..database import Database

class LikeService:
    def __init__(self, database: Database):
        self.database = database

    def add_like(self, user_id: int, property_id: int) -> Optional[Like]:
        query = """
        INSERT INTO property_likes (user_id, property_id, created_at)
        VALUES (%s, %s, %s)
        """
        try:
            cursor = self.database.connection.cursor()
            current_time = datetime.now()
            cursor.execute(query, (user_id, property_id, current_time))
            self.database.connection.commit()
            
            # Obtener el ID del like recién creado
            like_id = cursor.lastrowid
            
            return Like(
                id=like_id,
                user_id=user_id,
                property_id=property_id,
                created_at=current_time
            )
        except Exception as e:
            print(f"Error adding like: {e}")
            return None
        finally:
            cursor.close()

    def get_user_likes(self, user_id: int) -> List[Like]:
        query = """
        SELECT id, user_id, property_id, created_at
        FROM property_likes
        WHERE user_id = %s
        ORDER BY created_at DESC
        """
        try:
            results = self.database.execute_query(query, (user_id,))
            return [Like(**result) for result in results]
        except Exception as e:
            print(f"Error fetching user likes: {e}")
            return []
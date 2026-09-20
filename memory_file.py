from app.memory.database import (
    get_connection,
    initialize_database
)


def save_research(
    query: str,
    report: str
):

    initialize_database()

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO research_sessions
        (query, report)
        VALUES (?, ?)
        """,
        (
            query,
            report
        )
    )

    connection.commit()

    connection.close()


def get_previous_research(
    query: str,
    limit: int = 5
):

    initialize_database()

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            query,
            report,
            created_at
        FROM research_sessions
        WHERE query LIKE ?
        ORDER BY id DESC
        LIMIT ?
        """,
        (
            f"%{query}%",
            limit
        )
    )

    rows = cursor.fetchall()

    connection.close()

    return [
        {
            "query": row[0],
            "report": row[1],
            "created_at": row[2]
        }
        for row in rows
    ]
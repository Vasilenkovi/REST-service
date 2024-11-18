Simple service about beer based on DRF, for discipline "Технологии облачныз вычислений в бизнесе"

To deploy:
docker-compose up

URLs:
Swagger (openAPI) - based on drf-spectacular
http://127.0.0.1:8000/api/schema/swagger-ui/

[GET, POST]
http://127.0.0.1:8000/beer/ 

[GET, POST]
http://127.0.0.1:8000/shops/

[GET, PUT, PATCH, DELETE]
http://127.0.0.1:8000/beer/(id) 

[GET, PUT, PATCH, DELETE]
http://127.0.0.1:8000/shops/(id) 

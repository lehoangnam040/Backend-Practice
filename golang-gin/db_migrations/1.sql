
CREATE TABLE airport (
    id BIGSERIAL PRIMARY KEY,
    code VARCHAR(16),
    "name" VARCHAR(256)
);

-- Ingestion
INSERT INTO airport (code, "name") VALUES ('HAN', 'Noi Bai');
INSERT INTO airport (code, "name") VALUES ('SGN', 'Tan Son Nhat');
INSERT INTO airport (code, "name") VALUES ('PQC', 'Phu Quoc');
INSERT INTO airport (code, "name") VALUES ('DAD', 'Da Nang');
INSERT INTO airport (code, "name") VALUES ('CXR', 'Cam Ranh');
INSERT INTO airport (code, "name") VALUES ('VDO', 'Van Don');
INSERT INTO airport (code, "name") VALUES ('VCA', 'Can Tho');
INSERT INTO airport (code, "name") VALUES ('VCL', 'Chu Lai');
INSERT INTO airport (code, "name") VALUES ('THD', 'Tho Xuan');
INSERT INTO airport (code, "name") VALUES ('VDH', 'Dong Hoi');
INSERT INTO airport (code, "name") VALUES ('DIN', 'Dien Bien');
INSERT INTO airport (code, "name") VALUES ('TBB', 'Tuy Hoa');
INSERT INTO airport (code, "name") VALUES ('PXU', 'Pleiku');
INSERT INTO airport (code, "name") VALUES ('BMV', 'Buon Me Thuot');
INSERT INTO airport (code, "name") VALUES ('VKG', 'Rach Gia');
INSERT INTO airport (code, "name") VALUES ('CAH', 'Ca Mau');
INSERT INTO airport (code, "name") VALUES ('VCS', 'Con Dao');
INSERT INTO airport (code, "name") VALUES ('HUI', 'Phu Bai');
INSERT INTO airport (code, "name") VALUES ('VII', 'Vinh');
INSERT INTO airport (code, "name") VALUES ('UIH', 'Phu Cat');
INSERT INTO airport (code, "name") VALUES ('HPH', 'Cat Bi');
INSERT INTO airport (code, "name") VALUES ('DLI', 'Lien Khuong');

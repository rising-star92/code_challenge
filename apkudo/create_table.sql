CREATE TABLE Devices (
    id int,
    device_name varchar(50)
    count int,
    created_at Date
);

CREATE TABLE Invalid (
    id int,
    invalid_imei int,
    invalid_event int,
    created_at Date
)

CREATE TABLE FaultCode (
    id int,
    fault_code varchar(10)
    descriptioin varchar(50)
)
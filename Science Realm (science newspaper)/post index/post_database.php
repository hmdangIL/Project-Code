<?php
    class Database{
        private static $dbHost = "localhost";
        private static $dbName = "sciencerealm";
        private static $dbUser = "root";
        private static $dbUserPassword = NULL;
    
        private static $connection = NULL;

        public static function connect(){
            try{
                self::$connection = new PDO("mysql:host=".self::$dbHost."; dbname=".self::$dbName, self::$dbUser, self::$dbUserPassword);
            }
            catch(PDOException $e){
                die($e->getMessage());
            }
            return self::$connection;
        }
        public static function disconnect(){
            self::$connection = NULL;
        }
    }

    Database::connect();
        
?>
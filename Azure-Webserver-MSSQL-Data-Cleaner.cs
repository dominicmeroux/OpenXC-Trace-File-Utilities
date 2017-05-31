using System;
using System.Data;
using System.Data.SqlClient;
using System.Text;



namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create variables to read data into
            Int32 ID_result;
            DateTime LoggedTime_result;
            string JSONData;
            string JSONData2;
            Int32 Device_ID;
            // Try to access the Microsoft SQL database
            try
            {
                SqlConnectionStringBuilder builder = new SqlConnectionStringBuilder();
                builder.DataSource = "DATASOURCE_NAME.database.windows.net";
                builder.UserID = "DB_USERNAME";
                builder.Password = "DB_PASSWORD";
                builder.InitialCatalog = "DB_NAME"; 

                using (SqlConnection connection = new SqlConnection(builder.ConnectionString))
                {
                    Console.WriteLine("\nQuery data example:");
                    Console.WriteLine("=========================================\n");

                    connection.Open();
                    StringBuilder sb = new StringBuilder();
                    sb.Append("SELECT [Id], [LoggedTime], [Data], [LoggingDeviceId] "); // To select all entries
                    sb.Append("FROM [dbo].[LoggedData];");
                    String sql = sb.ToString();

                    using (SqlCommand command = new SqlCommand(sql, connection))
                    {
                        using (SqlDataReader reader = command.ExecuteReader())
                        {
                            JSONData2 = "";
                            while (reader.Read())
                            {
                                ID_result = reader.GetInt32(0);
                                LoggedTime_result = reader.GetDateTime(1);
                                JSONData = reader.GetString(2);
                                Device_ID = reader.GetInt32(3);
                                // Remove "{"records":[" and "]}"
                                JSONData2 = JSONData2 + JSONData.Replace(@"{""records"":[", "").Replace(@"]}", "");//.Replace(@"},", "},\n");
                                //
                                // TODO: IDENTIFY RECORDS ALREADY READ IN (BY ID???), INCLUDE LOGGER ID AND OTHER INFO IN OUTPUT...
                                //       ACCOMPLISH THIS BY LOOPING A QUERY??? THIS ISN'T NECESSARY IF YOU HAVE ONLY ONE C5 CELLULAR LOGGER. 
                                //       => while ID id the same, write to a filename with the logger ID appended, then switch to new file when that changes
                                //       => Another feature could be to delete entries from the database once they've been written to the CSV file
                                //
                                // 
                            }
                            // Properly paste JSON entries together, such that each line has the timestamp, name, and value, 
                            // and is seperated by a comma and newline character
                            JSONData2 = JSONData2.Replace(@"},", "},\n").Replace(@"}{", "},\n{").Replace(@"},{", "},\n{");
                            System.IO.File.WriteAllText(@"C:\Users\dmero\Desktop\WriteText.txt", JSONData2);
                            Console.WriteLine("Process Complete: Press any key to exit.");
                            Console.ReadKey();
                        }
                    }
                }
            }
            catch (SqlException e)
            {
                Console.WriteLine(e.ToString());
            }
        }
    }
}
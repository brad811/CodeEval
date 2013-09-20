import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Main
{
    static String ones[] = {
    		"","One","Two","Three","Four","Five","Six","Seven","Eight","Nine",
			"Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"};
	static String tens[] = {"","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"};
	static String commas[] = {"","Hundred","Thousand","Million"};
	
	public static void main(String[] args)
	{
		try
		{
			File file = new File(args[0]);
			BufferedReader in = new BufferedReader(new FileReader(file));
			String line;
			while ((line = in.readLine()) != null)
			{
				line = line.replace("\n", "");
				int number = Integer.parseInt(line);
				
				String output = "", newOutput = "";
				int n = 0;
				while(number > 0)
				{
					n++;
					if(n > 1)
					{
						newOutput = getThreeDigitNumber(number%1000);
						if(!newOutput.equals(""))
							output = newOutput + commas[n] + output;
					}
					else
					{
						newOutput = getThreeDigitNumber(number%1000);
						if(!newOutput.equals(""))
							output = newOutput + output;
					}
					number /= 1000;
				}
				
				System.out.println(output + "Dollars");
			}
			in.close();
		} catch (IOException e)
		{
			e.printStackTrace();
		}
	}
	
	static String getThreeDigitNumber(int number)
	{
		String output = "";
		if(number - number%100 > 0)
		{
			output += ones[(number - number%100)/100] + "Hundred";
		}
		if(number%100 < 20)
		{
			output += ones[number%100];
		}
		else
		{
			output += tens[(number%100 - number%10)/10];
			output += ones[number%10];
		}
		return output;
	}
}

from bs4 import BeautifulSoup 

soap_response = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Header><com:AUFHeaderRespo nse xmlns:com="http://schemas.auf.com/integration/common"><com:RequestId>C87892894718158925</co m:RequestId></com:AUFHeaderResponse></soapenv:Header><soapenv:Body><ns2:GetCustomer360Deta ilsResponse xmlns:ns2="http://schemas.auf.com/integration/customer"><ns2:TransactionStatus><com:ResponseCode xmlns:com="http://schemas.auf.com/integration/common">0</com:ResponseCode><com:ResponseMess age xmlns:com="http://schemas.auf.com/integration/common">Success</com:ResponseMessage><com:Exte ndedErrorDetails xmlns:com="http://schemas.auf.com/integration/common"><com:messages><com:code>0</com:code>< /com:messages></com:ExtendedErrorDetails></ns2:TransactionStatus><ns2:CustomerResponse><ns2:Cus tomerBasicInquiry><com:CustomerId xmlns:com="http://schemas.auf.com/integration/common">24047514213</com:CustomerId><com:Natio nalIdentificationCode xmlns:com="http://schemas.auf.com/integration/common">8751</com:NationalIdentificationCode><co m:CustomerName xmlns:com="http://schemas.auf.com/integration/common"><com:Prefix>MR.</com:Prefix><com:FirstNa me>RAJ</com:FirstName><com:LastName>KU</com:LastName><com:ShortName>SK</com:ShortName> <com:FormattedFullName>SUMAN##KU</com:FormattedFullName><com:FullName>SUMAN KU</com:FullName></com:CustomerName><com:CustomerFullName 
xmlns:com="http://schemas.auf.com/integration/common">SUMAN KU</com:CustomerFullName><com:OfficerID xmlns:com="http://schemas.auf.com/integration/common">First teller</com:OfficerID><com:CustomerAddress xmlns:com="http://schemas.auf.com/integration/common"><com:Line1>wwww</com:Line1><com:City> NEW DELHI</com:City><com:State>DELHI</com:State><com:Country>India</com:Country><com:Zip>110001</ com:Zip></com:CustomerAddress><com:BirthDateText xmlns:com="http://schemas.auf.com/integration/common">1976-06-03</com:BirthDateText><com:Categ oryType xmlns:com="http://schemas.auf.com/integration/common">INDIVIDUAL - FULL KYC</com:CategoryType><com:Sex xmlns:com="http://schemas.auf.com/integration/common">F</com:Sex><com:IsImageAvailable xmlns:com="http://schemas.auf.com/integration/common">true</com:IsImageAvailable><com:IsSignatur eAvailable xmlns:com="http://schemas.auf.com/integration/common">true</com:IsSignatureAvailable><com:Comb WithdrawBal xmlns:com="http://schemas.auf.com/integration/common">0.0</com:CombWithdrawBal><com:AgeOfCu stRel xmlns:com="http://schemas.auf.com/integration/common">2019-06-25</com:AgeOfCustRel><com:Home Branch xmlns:com="http://schemas.auf.com/integration/common">2143</com:HomeBranch><com:MobileNumb er xmlns:com="http://schemas.auf.com/integration/common">8903456566</com:MobileNumber><com:Em ailAddress xmlns:com="http://schemas.auf.com/integration/common">gdhs76dsban45@gmail.com</com:EmailAddr ess><com:IcType xmlns:com="http://schemas.auf.com/integration/common">L</com:IcType><com:IcTypeDesc xmlns:com="http://schemas.auf.com/integration/common">Lead Number</com:IcTypeDesc><com:BankShortName xmlns:com="http://schemas.auf.com/integration/common">Palanpur_Abu National Highway</com:BankShortName><com:PAN xmlns:com="http://schemas.auf.com/integration/common">AAYYT6574L</com:PAN><com:CustomerTyp e xmlns:com="http://schemas.auf.com/integration/common">100</com:CustomerType></ns2:CustomerBa sicInquiry></ns2:CustomerResponse><ns2:AccountDetails><com:CustomerAccount xmlns:com="http://schemas.auf.com/integration/common"><com:ModuleCode>C</com:ModuleCode><c om:ProductName>20234326-CURRENT ACCOUNT - RERA C</com:ProductName><com:AccountId>1921214323545891</com:AccountId><com:CASAAccountName> Raj Singhania</com:CASAAccountName><com:CurrencyCode>1</com:CurrencyCode><com:CurrencyShortNa me>INR</com:CurrencyShortName><com:CustomerRelationship>JAO</com:CustomerRelationship><com: BalanceBook>0.00</com:BalanceBook><com:UnclearFunds>0.00</com:UnclearFunds><com:Classification >NORMAL</com:Classification><com:Reason>UNBLOCKED</com:Reason><com:BillAmount>0.00</com:Bi llAmount><com:OriginalBalance>0.00</com:OriginalBalance><com:CurrentStatus>8</com:CurrentStatus> <com:CurrentStatusDescription>ACCOUNT OPEN REGULAR</com:CurrentStatusDescription><com:AcyAmount>0.00</com:AcyAmount><com:AvailableBala nce>0.00</com:AvailableBalance><com:LcyAmount>0.00</com:LcyAmount><com:TotalAcyAmount>0.00< /com:TotalAcyAmount><com:TotalLcyAmount>0.00</com:TotalLcyAmount><com:BranchName>Palanpur _Abu National Highway</com:BranchName><com:ExternalAccountId>0</com:ExternalAccountId><com:FutureDatedAm ount>0.00</com:FutureDatedAmount><com:SafeDepositBoxId>0</com:SafeDepositBoxId><com:DateAcc ountOpen>2019-06-25</com:DateAccountOpen><com:DateRelation>2019-06-25</com:DateRelation><co 
m:MonthsSinceActive>1</com:MonthsSinceActive><com:BalUncollectedPrinc>0.00</com:BalUncollected Princ><com:BalUncollectedInt>0.00</com:BalUncollectedInt><com:TotalBalUncollecPrinc>0.00</com:Tot alBalUncollecPrinc><com:TotalBalUncollecInt>0.00</com:TotalBalUncollecInt><com:TotalBalBook>0.00</c om:TotalBalBook><com:DateValue>2019-06-25</com:DateValue><com:BalPrincipal>0</com:BalPrincipal> <com:IntRate>0</com:IntRate><com:LienAmount>0</com:LienAmount><com:InstallmentAmount>0</co m:InstallmentAmount><com:OtherArrear>0</com:OtherArrear><com:BalCombinedAcy>0.0</com:BalCom binedAcy><com:BalCombinedLcy>0.0</com:BalCombinedLcy><com:BranchCode>2143</com:BranchCode ><com:IsTDLinkage>N</com:IsTDLinkage><com:HoldAmount>0</com:HoldAmount><com:ODLimitSaction ed>0</com:ODLimitSactioned><com:ODLimitUtilized>0</com:ODLimitUtilized><com:CASARelationshipDe tails><com:CustomerId>24047514</com:CustomerId><com:JointHolderName>Raj Singhania</com:JointHolderName><com:MobileNo>7021547608</com:MobileNo><com:Relationship>JAF </com:Relationship></com:CASARelationshipDetails><com:CASARelationshipDetails><com:CustomerId>2 4047513421</com:CustomerId><com:Emailid>gdhs45@gmail.com</com:Emailid><com:JointHolderName >SUMAN KU</com:JointHolderName><com:Relationship>JAO</com:Relationship></com:CASARelationshipDetails> <com:AmtGoal>0</com:AmtGoal><com:ProductCode>20236</com:ProductCode><com:Tenure>0 Months 0 Days 0 Years</com:Tenure></com:CustomerAccount><com:IsCustomerSchemeAvailable xmlns:com="http://schemas.auf.com/integration/common">false</com:IsCustomerSchemeAvailable></ns 2:AccountDetails></ns2:GetCustomer360DetailsResponse></soapenv:Body></soapenv:Envelope> 

"""

soup = BeautifulSoup(soap_response)

import requests

API_URL = "https://api.datayuge.com/v1/lookup/"

for each_number in soup.find_all('com:mobilenumb'):
    number = each_number.text
    res = requests.get(API_URL + number)
    print(f"Operator={res.json()['operator']} and Circle = {res.json()['circle']}")

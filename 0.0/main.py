import json
# from custom_functions.wwwwayfaircom import extract_wayfair_data, extract_wayfair_result
# from custom_functions.wwwwalmartcom import extract_walmart_data, extract_walmart_results
# from custom_functions.wwwmacyscom import extract_macys_data, extract_macys_results
# from custom_functions.wwwadidascom import extract_adidas_data, extract_adidas_results
# from custom_functions.wwwkohlscom import extract_kohls_data, extract_kohls_results
from custom_functions.wwwawaytravelcom import extract_awaytravel_data, extract_awaytravel_results
from custom_functions.wwwnikecom import extract_nike_data, extract_nike_results
from custom_functions.wwwultacom import extract_ulta_data, extract_ulta_results
from custom_functions.anovaculinarycom import extract_anovaculinary_data, extract_anovaculinary_result
from custom_functions.wwwdickssportinggoodscom import extract_dickssportinggoods_data, extract_dickssportinggoods_result

# Define a dictionary mapping authority names to extraction functions
extraction_functions = {
    # 'www.wayfair.com': (extract_wayfair_data, extract_wayfair_result),
    # 'www.walmart.com': (extract_walmart_data, extract_walmart_results),
    # 'www.macys.com': (extract_macys_data, extract_macys_results),
    # 'www.adidas.com': (extract_adidas_data, extract_adidas_results),
    # 'www.kohls.com': (extract_kohls_data, extract_kohls_results),
    'www.awaytravel.com': (extract_awaytravel_data, extract_awaytravel_results),
    'www.nike.com': (extract_nike_data, extract_nike_results),
    'www.ulta.com':(extract_ulta_data, extract_ulta_results),
    'anovaculinary.com': (extract_anovaculinary_data, extract_anovaculinary_result),
    'www.dickssportinggoods.com': (extract_dickssportinggoods_data, extract_dickssportinggoods_result)
}

def main():
    with open('input_urls.json', 'r') as file:
        input_data = json.load(file)
        success_data = []
        error_data = []
        for count, input_url in enumerate(input_data):
            print(count, input_url)
            with open('select_json_file.json', 'r') as file:
                json_data = json.load(file)
                for auth_item in json_data:
                    authority = auth_item.get('authority', '')
                    if authority in input_url:
                        # Extract the data and results based on the authority
                        extract_data_func, extract_results_func = extraction_functions.get(authority, (None, None))
                        if extract_data_func and extract_results_func:
                            try:
                                data_url = extract_data_func(input_url)
                                if data_url is None:
                                    # If data URL is None, store URL in error_data
                                    error_conf_data = {
                                        'title':None,
                                        'brand':None,
                                        'url':input_url
                                    }
                                    error_data.append(error_conf_data)
                                else:
                                    html_content = extract_results_func(data_url, input_url)
                                    if html_content is not None:
                                        success_data.extend(html_content)
                            except Exception as e:
                                if "404 Client Error" in str(e):
                                    # If 403 error is encountered, set title and brand to None and keep URL unchanged
                                    error_conf_data = {
                                        'title': None,
                                        'brand': None,
                                        'url': input_url
                                    }
                                    error_data.append(error_conf_data)
                                print(f"Error processing URL: {input_url}. Error: {e}")
                        else:
                            error_conf_data = {
                                'title': None,
                                'brand': None,
                                'url': input_url
                                }
                            error_data.append(error_conf_data)
        # Write success data to success_output.json
        with open('success_output.json', 'w') as file:
            json.dump(success_data, file, indent=4, default=str)
        # Write error data to error_output.json
        with open('error_output.json', 'w') as file:
            json.dump(error_data, file, indent=4, default=str)

if __name__ == "__main__":
    main()

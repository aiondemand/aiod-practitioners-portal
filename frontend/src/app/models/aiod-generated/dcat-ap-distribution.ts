/**
 * FastAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { DcatAPIdentifier } from './dcat-ap-identifier';


/**
 * Base class for all DCAT-AP objects
 */
export interface DcatAPDistribution { 
  [key: string]: any | any;


    id: any | null;
    type?: any | null;
    dcataccessURL?: any | null;
    dcatbyteSize?: any | null;
    spdxchecksum?: DcatAPIdentifier;
    dctdescription?: any | null;
    dcatdownloadURL?: any | null;
    dctformat?: any | null;
    dctlicense?: any | null;
    dcttitle?: any | null;
}

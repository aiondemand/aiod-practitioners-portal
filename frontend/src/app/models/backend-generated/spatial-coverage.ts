/**
 * AIoD - RAIL
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.20231219-beta
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { Geo } from './geo';
import { Address } from './address';


/**
 * A location that describes the spatial aspect of this dataset. For example, a point where all the measurements were collected.
 */
export interface SpatialCoverage {
    address?: Address;
    geo?: Geo;
}


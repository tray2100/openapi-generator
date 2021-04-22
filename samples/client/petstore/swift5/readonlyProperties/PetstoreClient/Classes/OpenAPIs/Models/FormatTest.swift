//
// FormatTest.swift
//
// Generated by openapi-generator
// https://openapi-generator.tech
//

import Foundation

public struct FormatTest: Codable, Hashable {

    public private(set) var integer: Int?
    public private(set) var int32: Int?
    public private(set) var int64: Int64?
    public private(set) var number: Double
    public private(set) var float: Float?
    public private(set) var double: Double?
    public private(set) var string: String?
    public private(set) var byte: Data
    public private(set) var binary: URL?
    public private(set) var date: Date
    public private(set) var dateTime: Date?
    public private(set) var uuid: UUID?
    public private(set) var password: String

    public init(integer: Int? = nil, int32: Int? = nil, int64: Int64? = nil, number: Double, float: Float? = nil, double: Double? = nil, string: String? = nil, byte: Data, binary: URL? = nil, date: Date, dateTime: Date? = nil, uuid: UUID? = nil, password: String) {
        self.integer = integer
        self.int32 = int32
        self.int64 = int64
        self.number = number
        self.float = float
        self.double = double
        self.string = string
        self.byte = byte
        self.binary = binary
        self.date = date
        self.dateTime = dateTime
        self.uuid = uuid
        self.password = password
    }

}

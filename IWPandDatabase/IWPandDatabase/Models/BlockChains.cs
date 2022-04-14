using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace IWPandDatabase.Models
{
    public class BlockChains
    {
        public int BlockID { get; set; }
        public string Nonce { get; set; }
        public string Data { get; set; }
        public string Prev { get; set; }
        public string Hash { get; set; }
    }
}